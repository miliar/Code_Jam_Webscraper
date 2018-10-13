#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

WIN = '1'
LOOSE = '0'
NOTHING = '.'

def team_stat(s,ignore_i=-1):
    wins = 0
    games = 0
    for i in range(len(s)):
        if i==ignore_i:
            continue
        c = s[i]
        if c==WIN:
            wins += 1
            games += 1
        if c==LOOSE:
            games += 1
#    wins = sum(map(lambda c: int(c==WIN), s))
#    games = sum(map(lambda c: int(c==WIN or c==LOOSE), s))
    return (wins,games)

def WP(s,ignore_i=-1):
    w, g = team_stat(s,ignore_i)
    return float(w) / float(g)

def RPI(WP,OWP,OOWP):
    return 0.25*WP + 0.5*OWP + 0.25*OOWP

def opponents(s):
    O = []
    for i in range(len(s)):
        c = s[i]
        if c!=NOTHING:
            O.append(i)
    return O

def average(A):
    return float(sum(A)) / float(len(A))

def solve(schedule):
    N = len(schedule)
    
    Opponents = [opponents(s) for s in schedule]
    
    WPs = [WP(s) for s in schedule]
    
    OWPs = [0]*N
    for i in range(N):
        WPis = [WP(schedule[o],i) for o in Opponents[i]]
        OWPs[i] = average(WPis)

    OOWPs = [0]*N
    for i in range(N):
        OWPis = [OWPs[o] for o in Opponents[i]]
        OOWPs[i] = average(OWPis)
        
#    print '   WP: ', WPs
#    print '  OWP: ', OWPs
#    print ' OOWP: ', OOWPs
    
    RPIs = [0]*N
    for i in range(N):
        RPIs[i] = RPI(WPs[i],OWPs[i],OOWPs[i])
        
    return RPIs

T = int(input.readline())
assert 1<=T and T<=20

for t in range(1,T+1):
    N = int(input.readline())
    assert 3<=N and N<=100
    
    schedule = []
    for n in range(N):
        S = input.readline().strip()
        assert len(S) == N
        assert all(map(lambda c: c in ['1','0','.'], S))
        schedule.append(S)
    
    rpis = solve(schedule)
    assert len(rpis) == N
    
    output.write('Case #%s:\n' % (str(t)))
    for rpi in rpis:
        output.write('%s\n' % (str(rpi)))
