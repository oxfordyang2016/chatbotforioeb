#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


def get_data(text):
    userId = '123456'
    inputText = {'text': text}
    key = 'your apiKey'
    userInfo = {'apiKey':"f8a3851b2aa8438298e685bd10bc4a4d", 'userId': "23235"}
    perception = {'inputText': inputText}
    data = {'perception': perception, 'userInfo': userInfo}
    return data


def get_answer(text):
    data = get_data(text)
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    response = requests.post(url=url, data=json.dumps(data))
    response.encoding = 'utf-8'
    result = response.json()
    answer = result['results'][0]['values']['text']
    return answer

