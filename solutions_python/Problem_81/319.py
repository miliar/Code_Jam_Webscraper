import sys

def RPI(WP, OWP, OOWP):
  return (0.25 * WP) + (0.5 * OWP) + (0.25 * OOWP)
  
def WP(team_info, skip_index):
  games_won = team_info["games_won"]
  total_games = team_info["total_games"]
  if (skip_index in team_info["opponents"]):
    total_games = total_games - 1
    if (skip_index in team_info["opponents_beaten"]):
      games_won = games_won - 1
  return (float(games_won) / float(total_games))
  
def OWP(team_index, game_info):
  total_opponent_WP = 0
  team_info = game_info[team_index]
  opponent_count = len(team_info["opponents"])
  for i in range(opponent_count):
    total_opponent_WP = total_opponent_WP + WP(game_info[team_info["opponents"][i]], team_index)
  return float(total_opponent_WP) / float(opponent_count)
  
def OOWP(team_index, game_info):
  total_opponent_OWP = 0
  team_info = game_info[team_index]
  opponents = team_info["opponents"]
  opponent_count = len(opponents)
  for i in range(opponent_count):
    opponent = game_info[opponents[i]]
    total_opponent_OWP = total_opponent_OWP + opponent["OWP"]
  return float(total_opponent_OWP) / float(opponent_count)

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  print ":"
  
  game_info = {}
  
  N = int(infile.readline())
  
  for i in range(N):
    game_info[i] = {}
    game_info[i]["total_games"] = 0
    game_info[i]["games_won"] = 0
    game_info[i]["opponents"] = []
    game_info[i]["opponents_beaten"] = []
    
    line = infile.readline()
    
    for j in range(N):
      if (line[j] == "1" or line[j] == "0"):
        game_info[i]["total_games"] = game_info[i]["total_games"] + 1
        game_info[i]["opponents"].append(j)
        if (line[j] == "1"):
          game_info[i]["games_won"] = game_info[i]["games_won"] + 1
          game_info[i]["opponents_beaten"].append(j)
    
    game_info[i]["WP"] = WP(game_info[i], i)

  for i in range(N):
    game_info[i]["OWP"] = OWP(i, game_info)
         
  for i in range(N):
    game_info[i]["OOWP"] = OOWP(i, game_info)
    
  for i in range(N):
    team_info = game_info[i]
    print RPI(team_info["WP"], team_info["OWP"], team_info["OOWP"])
  
infile.close()