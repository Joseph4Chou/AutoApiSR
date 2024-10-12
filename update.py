# -*- coding: UTF-8 -*-
import requests as req
import json
import sys
import time


path = sys.path[0]+r'/1.txt'


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
    with open(path, 'w+') as f:
        f.write(refresh_token)


def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    gettoken(refresh_token)


main()
