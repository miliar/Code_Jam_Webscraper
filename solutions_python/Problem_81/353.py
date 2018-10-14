#!/usr/bin/python
# -*- encode : utf8 -*-

import os
import sys

def openFile(fileName):
    f = open(fileName,'r')
    lines = f.readlines()
    f.close()
    return lines

if __name__ == '__main__':
    lines = openFile(sys.argv[1])
    
    i=1
    nn = 0
    while True:
        nn += 1
        N = int(lines[i].strip())
        i += 1
        cases = []
        WP = []
        OWP = []
        OOWP = []
        RIP = []
        for j in range(N):
            cases.append(list(lines[i+j].strip()))
        for j,v in enumerate(cases):
            wins = 0.0
            games = 0.0
            for vv in v:
                if vv == '1':
                    wins += 1.0
                if vv != '.':
                    games += 1.0
            WP.append(wins/games)

        for j,v in enumerate(cases):
            sum_WP4OWP = 0.0
            num = 0.0
            for jj,vv in enumerate(v):
                # WP4OWP
                if vv == '0' or vv == '1':
                    num += 1.0
                    wins = 0.0
                    games = 0.0
                    for jjj,vvv in enumerate(cases[jj]):
                        if jjj == j: continue
                        if vvv == '1': wins += 1.0
                        if vvv != '.': games += 1.0
                    sum_WP4OWP += wins/games
            OWP.append(sum_WP4OWP/num)

        for v in cases:
            tmp = 0.0
            num = 0.0
            for ii,vv in enumerate(v):
                if vv == '0' or vv == '1':
                    tmp += OWP[ii]
                    num += 1.0
            OOWP.append(tmp/num)
            
        for j in range(N):
            RIP.append(0.25*WP[j] + 0.50*OWP[j] + 0.25*OOWP[j])
        print 'Case #%d:' % nn
        for v in RIP:
            print v
        i += N
        if i >= len(lines): break