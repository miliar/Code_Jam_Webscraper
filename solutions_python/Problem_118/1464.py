#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math

def fair(i):
    if i != int(i):
        return False
    iStr = str(int(i))
    return iStr == iStr[::-1]

def fairAndSquare(i):
    return fair(i) and fair(math.sqrt(i))

def numberOfFairSquares(interval):
    result = 0
    for i in interval:
        if fairAndSquare(i):
            result += 1
    return result

f = open(sys.argv[1])
lines = f.readlines()
f.close()
for i in range(1, int(lines[0]) + 1):
    interval = lines[i].split(' ')
    interval = range(int(interval[0]), int(interval[1])+1)
    print 'Case #' + str(i) + ':', numberOfFairSquares(interval)