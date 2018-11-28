#!/usr/bin/python
#a.py
#Author: James Damore
#Created on: June 04, 2011
#Time-stamp: <2011-06-04 10:23:34>
#cat Downloads/A-small-attempt0.in | ~/python/codeJam/a.py > output.txt
#cat Downloads/A-large.in | ~/python/codeJam/a.py > output2.txt

import math
import string
import sys
import codejam as cj
import decimal
D = decimal.Decimal
from operator import itemgetter

def dbgln(a): sys.stderr.write(str(a) + "\n")
def read_ints(lines = None):
    if lines is None: return map(int, raw_input().split())
    return [map(int, raw_input().split()) for _ in range(lines)]
def array(size, default = None): return [default for _ in range(size)]
def matrix(r, c, default = None):
    return [array(c, default) for row in range(r)]


def read_input():
    X, S, R, t, N = read_ints()
    walkways = read_ints(N) #b, e, w
    walkways.sort(key=itemgetter(2))
    lengths = [e - b for b, e, w in walkways]
    totalW = sum(lengths)
    totalFree = X - totalW
    walkTimes = [(e - b) / (D(w) + S) for b, e, w in walkways]
    time = 0
    if totalFree / D(R) >= t:
        time += t
        totalFree -= R * t
        time += totalFree / D(S) + sum(walkTimes)
        return time
    time += totalFree / D(R)
    t -= time
    index = 0
    while t > 0 and index < N:
        if lengths[index] / D((walkways[index][2] + R)) <= t:
            time += lengths[index] / D((walkways[index][2] + R))
            t -= lengths[index] / D((walkways[index][2] + R))
            index += 1
        else:
            lengths[index] -= D((walkways[index][2] + R)) * t
            walkTimes[index] = lengths[index] / D(walkways[index][2] + S)
            time += t
            t = 0
    if index < N:
        time += sum(walkTimes[index:])
    return time


numCases=input()
for i in range(1, numCases+1):
    #read_input()
    dbgln(i)
    output = read_input()
    print "Case #%d:" % i, output
