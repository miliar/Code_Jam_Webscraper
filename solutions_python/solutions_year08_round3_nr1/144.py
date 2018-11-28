#!/usr/bin/env python

from sys import *
from re import *
from decimal import *
from math import *

def getInt():
    return int(stdin.readline())

def getInts():
    return map(int, stdin.readline().split())

N = getInt()
for case in range(N):
    [P, K, L] = getInts()
    freq = getInts()

    if Decimal(L)/Decimal(P) > K:
        print "Case #%d: Impossible" % (case+1)
        continue

    freq.sort()
    freq.reverse()

    pad = []
    for x in range(K):
        pad.append([])

    index = 0
    for f in freq:
        pad[index % len(pad)].append(f)
        index = index + 1

    sum = 0
    for key in range(len(pad)):
        for count in range(len(pad[key])):
            sum = sum + (count+1) * pad[key][count]

    print "Case #%d: %d" % (case+1, sum)
