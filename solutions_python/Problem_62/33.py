#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('rope.in','r')
T = int(fin.readline()[:-1])
for t in range(T):
    N = int(fin.readline()[:-1])
    ropes = []
    r = 0
    for n in range(N):
        new = [int(x) for x in fin.readline()[:-1].split()]
        for x in ropes:
            if (new[0] < x[0] and new[1] > x[1]) or (new[0] > x[0] and new[1] < x[1]):
                r += 1
        ropes += [new]
    print "Case #"+str(t+1)+": "+str(r)
