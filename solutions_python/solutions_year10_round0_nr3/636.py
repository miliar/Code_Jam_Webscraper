#!/usr/bin/python

from numpy import *

import os
import sys
import math

if len(sys.argv) < 2:
    print "Usage: ./themepark.py <inputfile>"
    sys.exit(0)

def calc (R, k, N, g):
#    print str(R) + " " + str(k) + " " + str(N)
#    print g
    starts = []
    next = []
    for i in range(N):
        count = 0
        j = i
        while 1 < 2:
            if count + g[j] > k:
                next.append(j)
                break
            else:
                count += g[j]
            j += 1
            if j == N:
                j = 0
            if j == i:
                next.append(j)
                break
        starts.append(count)
#    print starts
#    print next
    runs = []
    start = 0
    total = 0
    res = 0
    for i in range(R):
        runs.append(starts[start])
        total += starts[start]
        start = next[start]
        if start == 0:
            times = R / len(runs)
            res = total * times
            remaining = R % len(runs)
            for i in range(remaining):
                res += runs[i]
            break
    if start != 0:
        for i in range(len(runs)):
            res += runs[i]
    return res


inputFile = sys.argv[1]
input = fromfile (inputFile, int, -1, " ")
num = input[0]
start = 1
for i in range(num):
    R = input[start]
    k = input[start+1]
    N = input[start+2]
    g = input[start+3:start+3+N]
    start += 3+N
    res = calc(R, k, N, g)
    print "Case #" + str(i+1) + ": " + str(res)
