#!/usr/bin/env python
# coding: utf-8
import requests

jsonData = requests.get('https://reqres.in/api/users',verify=False)
if jsonData.status_code != 200:
    print("Error GET /tasks/ {}".format(jsonData.status_code))

names = []

for resp in jsonData.json()['data']:
    printData = [resp["first_name"],resp["last_name"]]
    names.append(' '.join(printData))

print(names)    #Final Answer
