#!/usr/bin/python

import sys

t = int(sys.stdin.readline())

def WP(team, teams, remove):
    sum = 0
    c = 0
    for t, i in enumerate(teams[team]):
        if t == remove:
            continue
        if i == '1':
            sum += 1
            c += 1
        elif i == '0':
            c += 1
    return float(sum) / c

def OWP(team, teams):
    sum = 0
    c = 0
    for i in range(len(teams)):
        if teams[i][team] == '.': continue
        if i == team: continue
        sum += WP(i, teams, team)
        c += 1

    return float(sum) / c

def OOWP(team, teams):
    sum = 0
    c = 0
    for i in range(len(teams)):
        if teams[i][team] == '.':
            continue
        if i == team:
            continue
        sum += OWP(i, teams)
        c += 1
    return float(sum) / c


def RPI(team, teams):
    return 0.25 * WP(team, teams, team) + 0.5 * OWP(team, teams) + 0.25 * OOWP(team, teams)

for ii in range(t):
    print "Case #%d:" % (ii+1)
    n = int(sys.stdin.readline())
    teams = n * ['']
    for j in range(n):
        teams[j] = sys.stdin.readline()
    for i in range(n):
        print RPI(i,teams)






