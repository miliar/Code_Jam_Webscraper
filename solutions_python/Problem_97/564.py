#!/usr/bin/python
#C.py
#Author: James Damore
#Created on: April 14, 2012
#Time-stamp: <2012-04-14 14:32:24>
#cat Downloads/C-large.in | ~/python/codeJam/C.py > output.txt

import math, sys
import codejam as cj

def dbgln(a): sys.stderr.write(str(a) + "\n")
def read_ints(lines = None):
    if lines is None: return map(int, raw_input().split())
    return [map(int, raw_input().split()) for _ in range(lines)]

N = 2000000
s = set()

for n in range(N):
    sn = str(n)
    for i in range(1, len(sn)):
        if sn[i] != '0':
            new = int(sn[i:] + sn[:i])
            if n < new:
                s.add((n, new))
s = sorted(s)

def read_input():
    A, B = read_ints()
    res = 0
    for n, m in s:
        if A <= n and m <= B:
            res += 1
        elif n >= B:
            break
    return res


numCases=input()
for i in range(1, numCases+1):
    #read_input()
    #dbgln(i)
    output = read_input()
    print "Case #%d:" % i, output
