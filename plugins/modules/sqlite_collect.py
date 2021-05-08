#!/usrmaster_list=Noneopyright: (c) 2020, Louis Tiches <ltiches@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#!/bin/python3
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: aquilon_man

short_description: This is my sqlite collect module

version_added: "1.0.0"

description: This is my longer description explaining my sqlite collect module.

options:
    name:
        description: This is the message to send to the sqlite collect module.
        required: true
        type: str

author:
    - Louis Tiches (ltiches@redhat.com)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.sqlite collect:
    name: hello world
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
my_useful_info:
    description: The dictionary containing information about your system.
    type: dict
    returned: always
    sample: {
        'foo': 'bar',
        'answer': 42,
    }
'''

import ansible.module_utils.basic
import sqlite3

import sqlite3
import os
from numpy import np

class SQ:
    def __init__(self, **kwargs):
        """
            db = SQ( [ table = ''] [, filename = ''] )
            constructor method
                table is for CRUD methods
                filename is for connecting to the database file
        """
        # see filename @property decorators below
        self._filename = kwargs.get('filename')

    def sql_query(self, sql, params=()):
            """
                db.sql_query( sql[, params] )
                generator method for queries
                    sql is string containing SQL
                    params is list containing parameters
                returns a generator with one row per iteration
                each row is a Row factory
                pick the datastructure
            """
            c = self._db.execute(sql, params)
            for r in c:
                yield r

    # filename property
    @property
    def _filename(self):
        return self._dbfilename

    @_filename.setter
    def _filename(self, fn):
        self._dbfilename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @_filename.deleter
    def _filename(self):
        self.close()

    def close(self):
        self._db.close()
        del self._dbfilename

class Sqlite_Data:
    def __init__(self, **kwargs):

        self._db_results = kwargs.get('db_results')
        self._target_list = kwargs.get('target_list')

    def sort_data_from_THIS_DATABASE(self, _db_results, _target_list):

        if target_list > 0:
            new_target_list = []
            for dict_iter in _target_list:
                for x in _db_results:


# noinspection PyCompatibility
def main():
    # define available arguments/parameters a user can pass to the module

    module_args = dict(
        hostname=dict(type='list', default=[], elements='str', required=False),
        personality=dict(type='lis', default=[], elements='str', required=False),
        rpm=dict(type='list', default=[], elements='str', required=False ),
    )

    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    hostname = module.params['hostname']
    personality = module.params['personality']
    rpm = module.params['rpm']

    test_hostname = length(hostname)
    test_personality = length(personality)

    db = SQ(filename=path, table=table)

    # contains all the hostnames and personalities

    Master_list = []
    no_hostname_list = []
    no_personality_list = []

    if test_personality > 0:

        path =
        db = SQ(filename=path)
        personality_tuple = tuple(personality)
        personality_query = "personality,hostname from hosts where personality in" + personality_tuple +";"

        if test_hostname == 0:
                for sql_iter in db.sql_query(personality_query):
                    dict_sql_iter = dict(sql_iter)
                    Master_list.append(dict_sql_iter)

                    if sql_iter.get('personality') not in personality and != None:
                        temp_personality = sql_iter.get('personality')
                        no_personality_list.append(temp_personality)
        else:

                for sql_iter in db.sql_query(personality_query):
                    dict_sql_iter = dict(sql_iter)
                    Master_list.append(dict_sql_iter)



    if test_hostname > 0:

        path =
        db = SQ(filename=path)
        hostname_tuple = tuple(hostname)
        hostname_query = "personality,hostname from hosts where personality in" + hostname_tuple + ";"

        if test_personality == 0:
            for sql_iter in db.sql_query(hostname_query):
                dict_sql_iter = dict(sql_iter)
                Master_list.append(dict_sql_iter)
                if sql_iter.get('hostname') not in personality and != None:
                    temp_hostname = sql_iter.get('hostname')
                    no_hostname_list.append(temp_hostname)

        else:
            for sql_iter in db.sql_query(hostname_query):
                dict_sql_iter = dict(sql_iter)
                Master_list.append(dict_sql_iter)


    if test_hostname > 0 and test_personality > 0:
        unique_master_list = np.array(Master_list)
        for data in combine_data:
            if data.get('personality') == None:
                temp_hostname = data.get('hostname')
                no_personality_list.append(temp_hostname)
            if data.get('hostname') == None:
                temp_personality = data.get('personality')
                no_hostname_list.append(temp_personality)

    unique_master_list = []
    compile_query = "select link_file,AQ7_inventory,personality,hostname,compile_result from compile_result where personality in" + personality_tuple +";"):
    for sql_iter in db.sql_query(compile_query):
        dict_sql_iter = dict(sql_iter)
        unique_master_list.append(dict_sql_iter)

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    
    if module.check_mode:
        module.exit_json(**unique_master_list)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    # result['original_message'] = module.params['name']
    # result['message'] = 'goodbye'
    # result['my_useful_info'] = {
    #     'foo': 'bar',
    #     'answer': 42,
    #}
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    
    module.exit_json(**unique_master_list)

if __name__ == '__main__':
    main()
