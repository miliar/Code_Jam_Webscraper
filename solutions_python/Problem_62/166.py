#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

trial = int(sys.stdin.readline())
for t in range(trial):
    n = int(sys.stdin.readline()) #wire
    ab = []
    for i in range(n): 
        ab.append([int(j) for j in sys.stdin.readline().split()])

    count = 0
    for c,i in enumerate(ab):
        for j in ab[c+1:]:
            if (i[0]<j[0] and i[1]>j[1]) or (i[0]>j[0] and i[1]<j[1]):
                count += 1
                
    print "Case #%d: %d"%(t+1, count)
