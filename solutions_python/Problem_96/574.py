#!/usr/bin/python
#B.py
#Author: James Damore
#Created on: April 14, 2012
#Time-stamp: <2012-04-14 13:51:19>
#cat Downloads/-small-attempt0.in | ~/python/codeJam/B.py > output.txt

import math, sys
import codejam as cj

def dbgln(a): sys.stderr.write(str(a) + "\n")
def read_ints(lines = None):
    if lines is None: return map(int, raw_input().split())
    return [map(int, raw_input().split()) for _ in range(lines)]


def read_input():
    ints = read_ints()
    N, S, p = ints[:3]
    T = ints[3:]
    output = 0
    for t in T:
        if t >= p + max(p - 1, 0) * 2:
            output += 1
        elif t >= p + max(p - 2, 0) * 2 and S > 0:
            output += 1
            S -= 1
    return output


numCases=input()
for i in range(1, numCases+1):
    #read_input()
    #dbgln(i)
    output = read_input()
    print "Case #%d:" % i, output
