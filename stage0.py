import requests
import json


TOKEN = "OTEzZmVhMmItYTg5Zi00ZmVmLWI4MGQtZDRmOGEzNjdlZjFiOTZjY2MzNzctZDM1_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

url = 'https://webexapis.com/v1/rooms'
headers= {'Authorization': f"Bearer {TOKEN}",
          'Content-Type': 'application/json'}


response=requests.get(url,headers=headers).json()
teams = response['items']
for team in teams:
    if team['title']== 'Programmability CTF - Day 1 - Team 1':
        teamId = team['id']
        print(team['title'],teamId)