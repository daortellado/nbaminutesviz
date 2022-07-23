from nba_api.stats.static import players
import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#init api

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#teamlist

team_list = ['76ers','Bucks','Bulls','Cavaliers','Celtics','Clippers','Grizzlies','Hawks','Heat','Hornets','Jazz','Kings','Knicks','Lakers','Magic','Mavericks','Nets','Nuggets','Pacers','Pelicans','Pistons','Raptors','Rockets','Spurs','Suns','Thunder','Timberwolves','TrailBlazers','Warriors','Wizards']

#outside api call to rosters

response = requests.get("https://data.nba.net/data/10s/prod/v1/2022/teams/kings/roster.json")
roster_data = response.json()

#parsin' to get list of ids for one team

player_list_dict = roster_data['league']['standard']['players']
player_list_ids = []
for i in range(len(player_list_dict)):
    player_list_ids.append(player_list_dict[i]['personId'])

#getting all player names

player_dict = players.get_players()

for i in range(0, len(player_list_ids)):
    player_list_ids[i] = int(player_list_ids[i])

print(player_list_ids)

#parse function

def id_lookup(player_id):
    player_name = [player for player in player_dict if player['id'] == player_id][0]['full_name']
    return player_name

#apply function to list of ids to get names

player_list_names=[]
for i in range(len(player_list_ids)):
    try:
        player_list_names.append(id_lookup(player_list_ids[i]))
    except:
        pass

print(player_list_names)

@app.get("/roster")
def get_roster():
  return player_list_names