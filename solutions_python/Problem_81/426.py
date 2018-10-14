#!/usr/bin/python

import re
import sys

input_file = open('A-large.in')
output_file = open('A-large.out', 'w')

T = int(input_file.readline())

def calc_WP(games):
    wins = 0
    num_games = 0
    for c in games:
        if c == '1' or c == '0':
            num_games += 1
        if c == '1':
            wins += 1
    return float(wins)/float(num_games)


for t in range(T):
    
    
    N = int(input_file.readline())
    teams = []
    for n in xrange(N):
        teams.append(input_file.readline().replace("\n", ""))
    
    ops = [list() for i in teams]
    
    for u in xrange(len(teams)):
        for i in xrange(len(teams[u])):
            if teams[u][i] == '1' or teams[u][i] == '0':
                ops[u].append(i)

    WP = []
    for team in teams:
        WP.append(calc_WP(team))

    WPm = [['.' for u in xrange(len(teams[i]))] for i in xrange(len(teams))]
    for i in xrange(len(teams)):
        for u in xrange(len(teams[i])):
            WPm[i][u]= calc_WP(teams[i][:u]+teams[i][u+1:])
            
    OWP = []
    for i in xrange(len(teams)):
        sum = 0
        for u in xrange(len(ops[i])):
            sum += WPm[ops[i][u]][i]
        OWP.append(float(sum)/float(len(ops[i])))
        
    OOWP = []
    for i in xrange(len(teams)):
        sum = 0
        for u in xrange(len(ops[i])):
            sum += OWP[ops[i][u]]
        OOWP.append(float(sum)/float(len(ops[i])))
        

    output_file.write("Case #" + str(t + 1) + ":\n")
    for i in xrange(len(teams)):
        output_file.write(str(.25 * WP[i] + .5 * OWP[i] + .25 * OOWP[i])+"\n")

input_file.close()
output_file.close()
