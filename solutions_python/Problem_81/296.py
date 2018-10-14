#!/usr/bin/env python

import sys

sys.stdin = open('in.txt')
sys.stdout = open('out.txt', 'w')

cases = int(input())

for caseno in range(1, cases+1):
    teams = int(input())
    table = [[-1 for i in range(teams)] for j in range(teams)]

    for n in range(teams):
        s = input()
        for i in range(teams):
            if s[i] != '.':
                num = int(s[i])
                table[n][i] = num

    wp = [-1 for i in range(teams)]
    owp = [-1 for i in range(teams)]
    oowp = [-1 for i in range(teams)]
    for i in range(teams):
        plays = 0
        wins = 0
        for j in table[i]:
            if j >= 0:
                plays += 1
            if j == 1:
                wins += 1
        wp[i] = wins/plays

    for i in range(teams):
        wps = []
        t = table[i]
        for j in range(teams):
            
            if t[j] >= 0 and i != j:
                plays = 0
                wins = 0
                for k in range(teams):
                    if table[j][k] >= 0 and k != i:
                        plays += 1
                        if table[j][k] == 1:
                            wins += 1
                wps.append(wins/plays)
        total = 0
        for w in wps:
            total += w
        owp[i] = total/(len(wps))

    for i in range(teams):
        owps = []
        for j in range(teams):
            if table[i][j] >= 0 and owp[j] >= 0:
                owps.append(owp[j])
        total = 0
        for j in owps:
            total += j
        assert len(owps) > 0
        oowp[i] = total / len(owps)
        

    print('Case #' + str(caseno) + ':')
    for i in range(teams):
        rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]
        print(rpi)
            
        
