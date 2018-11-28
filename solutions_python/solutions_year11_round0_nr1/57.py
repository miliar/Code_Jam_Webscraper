#!/usr/bin/env python

import sys
import math

def dist(a, b):
    if a - b < 0:
        return b - a
    return a - b

C = int(sys.stdin.readline())
for i in xrange(C):
    l = [x for x in sys.stdin.readline().split()][1:]
    couples = []
    for j in xrange(len(l)/2):
        couples.append((l[2*j], int(l[2*j+1])))
    prec = 'A'
    precv = 0
    pos = {}
    pos['O'] = 1
    pos['B'] = 1
    tot = 0
    for c in couples:
        if prec == c[0] or prec == 'A':
            tempo = dist(pos[c[0]], c[1]) + 1
            precv += tempo
        else:
            tempo = max(0, dist(pos[c[0]], c[1]) - precv) + 1
            precv = tempo
        pos[c[0]] = c[1]
        tot += tempo
        prec = c[0]

    print "Case #" + str(i+1) + ": " + str(tot)




