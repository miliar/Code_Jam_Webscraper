#!/usr/bin/env python3.2

def rpi(WP, OWP, OOWP):
  return 0.25*WP + 0.5*OWP + 0.25*OOWP

def wp(record):
  wins = 1.0*len([w for w in record if w == '1'])
  total = 1.0*len([w for w in record if w == '1' or w == '0'])
  return wins/total

def owp(games, i):
  N = len(games)
  wps = []
  ws = []
  for team in range(0,len(games)):
    if games[team][i] != '.' and team != i:
      ws.append(games[team][:])
  games = ws
  for team in games:
    del team[i]
  return sum([wp(r) for r in games])/len(games)

def oowp(owps, games, i):
  owpsum = 0.0
  N = len(games)
  count = 0
  for team in range(0,N):
    if team != i and games[team][i] != '.':
      owpsum += owps[team]
      count += 1
  return owpsum/count

def solve(games):
  wps = [wp(r) for r in games]
  owps = [owp(games, i) for i in range(0, len(games))]
  oowps = [oowp(owps, games, i) for i in range(0, len(games))]

  for i in range(0, len(games)):
    print(rpi(wps[i], owps[i], oowps[i]))

if __name__ == "__main__":
  import sys
  T = int(sys.stdin.readline())
  for t in range(1, T+1):
    print('Case #{0}: '.format(t))
    N = int(sys.stdin.readline())
    games = [list(sys.stdin.readline().replace("\n",'')) for i in range(0,N)]
    solve(games)


