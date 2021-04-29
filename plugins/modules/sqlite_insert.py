#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Louis Tiches
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import yaml
from ansible.module_utils.basic import AnsibleModule
from ansible.errors import AnsibleError, AnsibleParserError

try:
    import sqlite3
except AnsibleParserError():
    raise AnsibleError("Please install sqlite3")

def path_test(file_path):
    if not os.path.exists(file_path):
        module.fail_json(msg="file not found: %s" % source)

def conn(path,q):
    curse = sqlite3.connect(path).cursor()
    vv = curse.execute(q)
    conn = list(vv)
    return conn

def row_finder(x):
    d = x[0]
    l = len(x)
    ret = [[],[],[]]
    if not isinstance(d,dict):
        raise Exception("Please install sqlite3")
    key_list = []
    for d in x:
        for k,v in d.items():
            key_list.append(k)
            ret[2].append((v))
            ret[1].append((k,v))
    ret[0].append(set(key_list))
    return ret

def query_table(ret):
    key = list(ret[0][0])
    value = ret[1]
    table_results = []
    for k in key:
        in_list = []
        for v in value:
            if k == v[0]:
                in_list.append(v[1])
        if len(in_list) == 1:
            x = str(in_list[0])
            temp_tup = "('" + x + "')"
        else:
            temp_tup = tuple(in_list)
        table_results.append('OR')
        x = k + ' in ' + str(temp_tup)
        table_results.append(x)


    table_results.pop(0)
    x = " ".join(table_results)
    query_results = "select * from genres where "+ x + ";"
    return query_results

def state_test(path,q):
    connector(path,q)
    
def sort(tup):
    lst = []
    if not isinstance(tup[0], str) or isinstance(tup[0], int):
        for x in tup:
            for u in x:
                lst.append(u)
    else:
        lst = tup
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst ]
    return lst

def main():
    module_args = dict(
        rows=dict(type='list', required=True),
        path=dict(type='str', required=True),
        table=dict(type='str', required=True),
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    table = module.params['table']
    path = module.params['path']
    rows = module.params['rows']


    path_test(path)
    ret = row_finder(rows)
    q = query_table(ret)
    curse = sqlite3.connect(path).cursor()
    change = list(curse.execute(q))
    current = ret[2]
    c1 = sort(current)
    c2 = sort(change)

    if c1 != c2:
        result['changed'] = True
        result['diff'] = dict(
            before=yaml.safe_dump(c1),
            after=yaml.safe_dump(c2)
        )

    # Update database

    if module.check_mode or not result['changed']:
        module.exit_json(**result)

    module.exit_json(**result)

if __name__ == '__main__':
    main()
