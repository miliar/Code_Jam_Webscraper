#!/usr/bin/python

import sys



def flip(pan, K):
    moves = 0
    s = 0
    e = len(pan)
    #print "**        ", pan, e,s, e-s, K
    if (e-s) < K:
        for o in range(0,e):
            if pan[o] == '-':
                return -1
        return 0

    e -= K -1
    for o in range(s, e):
        if pan[o] == '-':
            #print 'before', o, e, pan[o:]
            f = o
            if f < e:
                #flip with K
                for i in range(f,f+K):
                    pan[i] = '+' if pan[i] == '-' else '-'
                moves += 1
                s += 1
            #print 'after ', o, e, pan[o:]

    #print e,K,pan[e:]
    for o in range(e, e+K-1):
        if pan[o] == '-':
            return -1
    return moves


tc = raw_input()

pans = []

for line in sys.stdin.readlines():
    pan, K = line.strip().split(' ')
    pans.append((list(pan), int(K)))


tc = 0
for pan, K in pans:
    tc += 1
    cnt = flip(pan, K)
    print "Case #%s: %s" % (tc, "IMPOSSIBLE" if cnt < 0 else cnt)
