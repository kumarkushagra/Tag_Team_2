import json
import pprint
import requests

INSTANCE =  "263a8669-40edbe8f-11ca99f2-0586ac60-9f6f1dcb"
OVERWRITE_INSTANCES = True   # Whether the "OverwriteInstance" is set to "true" in the Orthanc config

r = requests.post('http://localhost:8042/instances/%s/modify' % INSTANCE, json.dumps({
    'Replace' : {
        'PatientName' : 'RENAME SUCCESSFULL'
    },
    'Keep' : [ 'SOPInstanceUID' ],  # Don't generate a new SOPInstanceUID
    'Force' : True                  # Mandatory if SOPInstanceUID must be kept constant
    }))

r.raise_for_status()

dicom = r.content

if not OVERWRITE_INSTANCES:
    r = requests.delete('http://localhost:8042/instances/%s' % INSTANCE)
    r.raise_for_status()

r = requests.post('http://localhost:8042/instances', dicom)
r.raise_for_status()
pprint.pprint(r.json())