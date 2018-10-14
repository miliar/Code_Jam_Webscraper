
from msvcrt import getch

def window(l, n):
  for i in range(0, len(l)-n+1):
    yield l[i:(i+n)]

def chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:(i+n)]

file_in = open("A-large.in", "r")
file_out = open("A.out", "w")
cases_ct = int( file_in.readline() )

for case_num in range(1, cases_ct+1):
  team_ct_raw = file_in.readline().strip()
  print(team_ct_raw)
  teams = int(team_ct_raw)
  team_records = []
  wps = []
  owps = []
  oowps = []
  tot_wins = []
  tot_games = []
  for i in range(0,teams):
    team_record = file_in.readline().strip() 
    print(team_record)
    team_records.append( team_record )
    wins = 0
    losses = 0
    for game in team_record:
      if game == "1":
        wins += 1
      elif game == "0":
        losses += 1
    tot_wins.append( wins )
    tot_games.append( wins+losses )
    wps.append( wins / (wins+losses) )
  
  print(wps)
  for i in range(0,teams):
    owp = 0
    adjust_wps = 0
    tot_teams = 0
    for j in range(0,teams):
      if i == j:
        continue
      if team_records[i][j] == ".":
        continue
      tot_teams += 1
      if team_records[j][i] == "1":
        adjust_wps = (tot_wins[j] - 1) / (tot_games[j] - 1)
      elif team_records[j][i] == "0":
        adjust_wps = (tot_wins[j]) / (tot_games[j] - 1)
      else:
        adjust_wps = wps[j]
      owp += adjust_wps
    if tot_teams == 0:
      owp = 0
    else:
      owp = owp / tot_teams
    owps.append(owp)
  print(owps)
  
  for i in range(0,teams):
    oowp = 0
    tot_teams = 0
    for j in range(0,teams):
      if i == j:
        continue
      if team_records[i][j] == ".":
        continue
      tot_teams += 1
      oowp += owps[j]
    if tot_teams == 0:
      oowp = 0
    else:
      oowp = oowp / tot_teams
    oowps.append(oowp)
  print(oowps)
  
  file_out.write("Case #{0}:\n".format(case_num) )
  for i in range(0,teams):
    file_out.write("{0}\n".format(0.25 * wps[i] + 0.50 * owps[i] + 0.25 * oowps[i]))
