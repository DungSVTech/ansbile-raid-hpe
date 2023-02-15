curl -k -v -u 'admin:admin123' -H 'Accept: application/json'  -H 'Cache-Control: no-cache' -H 'Content-Type: application/json' -X PUT https://10.1.17.3/redfish/v1/systems/1/smartstorageconfig/settings -d '{ "DataGuard":"Disabled", "LogicalDrives": [ {"Raid": "Raid1", "DataDrives": [ "1I:1:2","1I:1:3" ], "LogicalDriveName": "LogicalSV03", "Raid": "Raid1", "SpareDrives": [] } ] }'

