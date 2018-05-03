import json
import random
import requests

from django.shortcuts import render
from django.http import HttpResponse

from bot.load_serif import osomatsu_serif

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = 'B+CR4QA0nUSM9IA8hLcXjSueqDUSeaLUI5s9bRgWzz9aEF8ujFMqklsMc8LkNegKKJEQzq5qkF915479CGI04ptrreYwTPPImn8kXXLl2GK20Y1yqUvFkDwFVtK+Ty5B1CQzPRo+3lMAYMxi5a04dAdB04t89/1O/w1cDnyilFU='
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("This is bot api.")

def reply_text(reply_token, text):
    reply = random.choice(osomatsu_serif)
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": reply
                }
            ]
    }

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
    return reply

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token = e['replyToken']
        message_type = e['message']['type']

        if message_type == 'text':
            text = e['message']['text']
            reply += reply_text(reply_token, text)
    return HttpResponse(reply)
