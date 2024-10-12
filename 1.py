# -*- coding: UTF-8 -*-
import requests as req
import json
import sys
import time
import random


path = sys.path[0]+r'/1.txt'
num1 = 0


def gettoken(refresh_token):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'
               }
    data = {'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': id,
            'client_secret': secret,
            'redirect_uri': 'http://localhost:53682/'
            }
    html = req.post(
        'https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data, headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    return access_token


def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    global num1
    localtime = time.asctime(time.localtime(time.time()))
    access_token = gettoken(refresh_token)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    print('此次运行开始时间为 :', localtime)
    try:
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root', headers=headers).status_code == 200:
            num1 += 1
            print("1调用成功"+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive', headers=headers).status_code == 200:
            num1 += 1
            print("2调用成功"+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/drive/root', headers=headers).status_code == 200:
            num1 += 1
            print('3调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/users', headers=headers).status_code == 200:
            num1 += 1
            print('4调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/messages', headers=headers).status_code == 200:
            num1 += 1
            print('5调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules', headers=headers).status_code == 200:
            num1 += 1
            print('6调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules', headers=headers).status_code == 200:
            num1 += 1
            print('7调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers).status_code == 200:
            num1 += 1
            print('8调用成功'+str(num1)+'次')
        if req.get(r'https://api.powerbi.com/v1.0/myorg/apps', headers=headers).status_code == 200:
            num1 += 1
            print('8调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders', headers=headers).status_code == 200:
            num1 += 1
            print('9调用成功'+str(num1)+'次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories', headers=headers).status_code == 200:
            num1 += 1
            print('10调用成功'+str(num1)+'次')
    except:
        print("pass")
        pass


for _ in range(6):
    main()
    for i in range(random.randint(600, 1200), 0, -1):
        time.sleep(1)
