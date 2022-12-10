#basic version of file upload request
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
        data=json.load(f)   #read data from json file

    sensordata=data['sensor_details']
    
    for i in sensordata:
        header=i.keys()
    emplist.append(list(header)) #Append headers to the list
    for i in sensordata:
        j=list(i.values())
        for k in j:
            emplist.append(k)
    print('The list is:',emplist)  #final nested list with each sublist containing data for one particular metric

    def transpose(lists):  #function to transpose the nested list where each sublist contains one data unit for each metric
        global uploadobj
        if not lists:
            return []
        uploadobj=map(lambda *row: list(row), *lists)
        uploadobj=list(uploadobj)
        print(uploadobj)
    transpose(emplist[1:])


def upload_variable(): #function to upload data to server
    r=requests.post('http://52.207.196.214/api/v1/upload',json={'data':str(emplist[0])})  #upload headers first
    r=requests.post('http://52.207.196.214/api/v1/upload',json={'data':str(uploadobj)})   #upload transposed data 
    print('upload status code:',r.status_code)
    if r.ok:
        print(" File uploaded successfully ! ")
        print(r.text)  #print upload status
        for i in r:
            print(i)
    else:       
        print(" Please Upload again ! ")

def download_data():  #download data from server to computer
    r=requests.get('http://52.207.196.214/api/v1/download')
    print(r.text)

convert_json_to_csv()
upload_variable()
download_data()
