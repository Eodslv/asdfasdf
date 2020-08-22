import json
import discord
import requests
import datetime
from urllib.request import urlopen

rank = 1

#Matsurihime Parsing

EventLink = requests.get('https://api.matsurihi.me/mltd/v1/events')
__Temp = EventLink.json()
LastEventData = __Temp[-1]

def JPEventBorderData() :
    BorderLink = requests.get('https://api.matsurihi.me/mltd/v1/events/%s/rankings/logs/eventPoint/%s'%(LastEventData['id'],'1,100,2500,5000'))
    __Temp = BorderLink.json()
    return __Temp[0]['data'][-1]['summaryTime'],__Temp[0]['data'][-1]['score'], __Temp[1]['data'][-1]['score'], __Temp[2]['data'][-1]['score'], __Temp[3]['data'][-1]['score']

def JPEventHBorderData() :
    BorderLink = requests.get('https://api.matsurihi.me/mltd/v1/events/%s/rankings/logs/highscore/%s'%(LastEventData['id'],'1,100,2000,5000,10000,20000'))
    __Temp = BorderLink.json()
    return __Temp[0]['data'][-1]['summaryTime'],__Temp[0]['data'][-1]['score'], __Temp[1]['data'][-1]['score'], __Temp[2]['data'][-1]['score'], __Temp[3]['data'][-1]['score'], __Temp[4]['data'][-1]['score'], __Temp[5]['data'][-1]['score']

def JPEventTimeData() :
    return LastEventData['name'], LastEventData['schedule']['beginDate'], LastEventData['schedule']['endDate']

token = "NzAyODA1Nzg1NzM0MDIxMTkx.XqVTPw.McvVtKcc5J2Cn75Qbl7ACFSDsxg"
client = discord.Client()

#Discord
@client.event
async def on_ready(): 
  await client.change_presence(status=discord.Status.online)
  print("I'm Ready!") # I'm Ready! 문구를 출력합니다.
  print(client.user.name) # 봇의 이름을 출력합니다.
  print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.

@client.event
async def on_message(message) :
    channel = message.channel
    if message.content == "!정보" :
        EventTimeVar = JPEventTimeData()
        await channel.send("🎤 현재 진행중인 이벤트 🎤 \n%s\n\n▶ 시작 : %s\n▶ 종료 : %s"%(EventTimeVar[0],EventTimeVar[1],EventTimeVar[2]))
    
    if message.content == "!랭킹" :
        EventBData = JPEventBorderData()
        await channel.send("📈 포인트 안내 📈\n최종 업데이트 : %s\n\n▶ 1위 : %d점\n▶ 100위 : %d점\n▶ 2500위 : %d점\n▶ 5000위 : %d점"%(EventBData[0],EventBData[1],EventBData[2],EventBData[3],EventBData[4]))

    if message.content == "!하이스코어" :
        EventHBData = JPEventHBorderData()
        await channel.send("📊 하이스코어 안내 📊\n최종 업데이트 : %s\n\n▶ 1위 : %d점\n▶ 100위 : %d점\n▶ 2000위 : %d점\n▶ 5000위 : %d점\n▶ 10000위 : %d점\n▶ 20000위 : %d점"%(EventHBData[0],EventHBData[1],EventHBData[2],EventHBData[3],EventHBData[4],EventHBData[5],EventHBData[6]))

    if message.content == "!명령어" :
        await channel.send("!정보 : 일섭 이벤트 정보\n!랭킹 : 일섭 랭킹 정보 (~5000)\n!하이스코어 : 일섭 하이스코어 정보 (~5000)")


    
client.run(token)
