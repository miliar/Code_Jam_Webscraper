#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(C, farmProduction, X):
    curTime = 0
    curSpeed = 2.0
    bestTime = X / curSpeed
    initTime = bestTime
    if C >= X:
        return bestTime
    while curTime <= initTime:
        curTime += C / curSpeed
        curSpeed = curSpeed + farmProduction
        newTime = curTime + X / curSpeed
        if bestTime < newTime:
            return bestTime
        bestTime = newTime
    return bestTime

import sys

sys.stdin.readline()

for i, line in enumerate(sys.stdin, 1):
    c, f, x = map(float, line.strip().split())
    print "Case #{}: {}".format(i, solve(c, f, x))
