import sys
from copy import copy
from collections import deque
from time import sleep

qty_test_cases = int(sys.stdin.readline())

def getWP(team_data):
    games_played = [x for x in team_data if x != "."]
    games_won = games_played.count("1")
    
    return games_won / float(len(games_played))

def getOWP(teams, exclude):
    accumulated_wp = 0.0
    
    rng = range(0, len(teams))
    j = 0
    
    for i in rng:
        if teams[exclude][i] != ".":
            partial_team = copy(teams[i])
            del partial_team[exclude]
            accumulated_wp += getWP(partial_team)
            j+=1
    
    return accumulated_wp / j

def getOOWP(teams, exclude):
    accumulated_owp = 0.0
    
    rng = range(0, len(teams))
    j = 0

    for i in rng:
        if teams[exclude][i] != ".":
            accumulated_owp += getOWP(teams, i)
            j+=1

    return accumulated_owp / j

for i in range(qty_test_cases):
    print "Case #%d:" % (i+1)
    
    qty_teams = int(sys.stdin.readline())
    teams = list()
    
    for i in range(0, qty_teams):
        teams.append( list(sys.stdin.readline().strip())[0:qty_teams] )
    
    for team_index in range(qty_teams):
        rpi = 0.25 * getWP(teams[team_index]) + 0.50 * getOWP(teams, team_index) + 0.25 * getOOWP(teams, team_index)
        print rpi
