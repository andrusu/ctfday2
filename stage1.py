import requests
import json


TOKEN = "OTEzZmVhMmItYTg5Zi00ZmVmLWI4MGQtZDRmOGEzNjdlZjFiOTZjY2MzNzctZDM1_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

room_url = 'https://webexapis.com/v1/rooms'
headers= {'Authorization': f"Bearer {TOKEN}",
          'Content-Type': 'application/json'}

room_body={
    "title":"Collab CTF day 2 - Andrea"
}

#room_post=requests.post(room_url,headers=headers, data=json.dumps(room_body)).json()
#print(room_post)  # < created the room
room_get=requests.get(room_url,headers=headers).json()
rooms = room_get['items']
for room in rooms:
    if room['title']== 'Collab CTF day 2 - Andrea':
        roomId = room['id']
        print(room['title'],roomId)  # returns id


msg_url = 'https://webexapis.com/v1/messages'     #message the room
msg_body= {
    'roomId': roomId,
    'text':'Hi!'
}

#msg_response=requests.post(msg_url, headers=headers, data=json.dumps(msg_body)).json()

#add people to the space

add_url='https://webexapis.com/v1/memberships'
add_body={
    'roomId': roomId,
    'personEmail':'',
    'isModerator': False 
}

add_response=requests.post(add_url, headers=headers, data=json.dumps(add_body)).json()
