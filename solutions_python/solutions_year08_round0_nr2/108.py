#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

A_TO_B = 0
B_TO_A = 1

def hours2minutes(s):
    h, m = map(int, s.split(':'))
    return 60*h + m

cases = int(sys.stdin.readline())

for case in xrange(cases):
    ttime  = int(sys.stdin.readline())
    NA, NB = map(int, sys.stdin.readline().strip().split())

    trips      = [map(hours2minutes, sys.stdin.readline().strip().split()) + [A_TO_B] for i in xrange(NA)]
    trips.extend([map(hours2minutes, sys.stdin.readline().strip().split()) + [B_TO_A] for i in xrange(NB)])
    trips.sort(lambda x,y: x[0]-y[0])

    trainStart = [0, 0]
    trains     = [[], []]
    for start, end, d in trips:
        #print trains
        #print trainStart
        #print start,end,d
        #print
        if len(trains[d]) == 0 or trains[d][0] > start:
            trainStart[d] += 1
        else:
            trains[d].pop(0)
        trains[int(not d)].append(end + ttime)
        trains[int(not d)].sort()
    print "Case #%d: %d %d" % (case+1, trainStart[0], trainStart[1])
