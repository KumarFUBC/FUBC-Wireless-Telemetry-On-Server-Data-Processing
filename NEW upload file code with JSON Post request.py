'''
import requests
import csv
dfile=open("data_csv.csv", "rb")
url = "http://52.207.196.214/api/v1/upload"
test_res = requests.post(url, files = {"form_field_name": dfile})
if test_res.ok:
    print(" File uploaded successfully ! ")
    print(test_res.text)
else:
    print(" Please Upload again ! ")
'''

# new version of file upload with JSON post request
import json
import requests

def convert_json_to_csv():
    global emplist
    global sensordata
    emplist=[]
    with open('sensor_data.json') as f:
        data=json.load(f)

    sensordata=data['sensor_details']
    count=0
    
    for i in sensordata:
        if count==0:
            header=i.keys()
            count+=1
    emplist.append(list(header))
    for i in sensordata:
        j=list(i.values())
        for k in j:
            emplist.append(k)
    print('The variable emplist contains: ',emplist) 

def upload_variable():
    r=requests.post('http://52.207.196.214/api/v1/upload',json={'data':emplist})#using "emplist" did not work, it just uploaded the word "emplist" as a string. 
                                                                                #I'm not sure if we should use it as it is or use str(emplist). Doing that gives 
                                                                                #status code 504.
    print('upload status code:',r.status_code)
    if r.ok:
        print(" File uploaded successfully ! ")
        print(r.text)
        for i in r:
            print(i)
    else:   
        print(" Please Upload again ! ")

def download_data():
    r=requests.get('http://52.207.196.214/api/v1/download')
    print(r.text)


