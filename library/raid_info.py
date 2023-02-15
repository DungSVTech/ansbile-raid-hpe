#!/usr/bin/python

import json
import requests
from ansible.module_utils.basic import *
from ansible.module_utils.basic import AnsibleModule

def update_hpe_raid(**args):

    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Cache-Control': 'no-cache'  
    }

    auth = requests.auth.HTTPBasicAuth(args['username'], args['password'])

    #session = requests.Session()
    #session.auth = (args['username'], args['password'])
    #session.headers.update({'Content-Type': 'application/json'})

    # Get the root endpoint
    root_endpoint = "https://" + args['host'] + "/redfish/v1/"
    # Get the Storage endpoint
    response = requests.get(root_endpoint + "Systems/1/smartstorageconfig", headers = headers , auth = auth , verify=False)

    # get devices information  
    devices_info = response.json()
    datadrives = [ i['Location'] for i in devices_info['PhysicalDrives'] ]


    # payload to create raid
    payload = {
       "DataGuard" : args['dataguard'],
       "LogicalDrives": [
           { 
             "Raid": args['raid'],
	     "LogicalDriveName": args['logicaldrivename'],
             "DataDrives": datadrives,
       	     "SpareDrives": []
           }
	]
    }

    response_create_raid = requests.put(root_endpoint + "Systems/1/smartstorageconfig/settings", headers = headers , auth = auth , data = json.dumps(payload), verify=False)  
    


    return True, response_create_raid.content

def main():

   
   fields = {
       "host": { "required": True, "type": "str" },
       "username": { "required": True, "type": "str" },
       "password": { "required": True, "type": "str" },
       "raid": { "required": True, "type": "str" },
       "dataguard": { "required": True, "type": "str" },
       "logicaldrivename": { "required": True, "type": "str" },


   }

   module = AnsibleModule( 
       argument_spec = fields,
   )
   args = module.params
   has_changed, result = update_hpe_raid(**args) 
   module.exit_json(changed= has_changed, result= result)
   module.fail_json(msg="Something fatal happened")
	
if __name__ == '__main__':
   main()
