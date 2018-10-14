#!/usr/bin/env python

f = open("A-large.in")
test_size = int(f.readline())


def calcWP(team):
    matchNum = 0
    winNum = 0.0
    for i in range(len(team)):
        if team[i] != ".":
            matchNum += 1
        if team[i] == "1":
            winNum += 1
#    print winNum / matchNum
    return winNum / matchNum

def calcOWP(teams, myTeam):
    teamNum = 0
    wpSum = 0.0
    for x in range(len(teams)):
        if myTeam != x and teams[myTeam][x] != ".":
            teamNum += 1
            t = teams[x][:]
            t.pop(myTeam)
#            print t
            wpSum += calcWP(t)
#    print wpSum / teamNum
    return wpSum / teamNum



def calcOOWP(OWP, myTeam, teams):
    teamNum = 0
    owpSum = 0.0
    for x in range(len(teams)):
        if myTeam == x or teams[myTeam][x] == ".":
            continue
        teamNum += 1
        owpSum += OWP[x]
#    print owpSum / teamNum
    return owpSum / teamNum

def calcRPI(WP, OWP, OOWP, myTeam):
    return WP[myTeam] * 0.25 + OWP[myTeam] * 0.50 + OOWP[myTeam] * 0.25

for x in range(1, test_size + 1):
    teamsNum = int(f.readline())
    teams = []
    WP = []
    OWP = []
    OOWP = []
    for i in range(teamsNum):
        teams.append(list(f.readline().strip()))
        WP.append(calcWP(teams[i]))

    for i in range(teamsNum):
        OWP.append(calcOWP(teams, i))

    for i in range(teamsNum):
        OOWP.append(calcOOWP(OWP, i, teams))

    print "Case #%d:" % x
    for i in range(teamsNum):
        print calcRPI(WP, OWP, OOWP, i)