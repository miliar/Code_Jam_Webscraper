#!/bin/env python

# google code jam 2017 qualifiers problem 2
# Daniel Scharstein

import sys

def sub1(r, i):
    if r[i] > 0 and (i == 0 or r[i] > r[i-1]):
        r[i] -= 1
    else:
        r[i] = 9
        sub1(r, i-1)

def solve(s):
    r = [int(x) for x in s]
    #print r
    n = len(r)
    nines = False
    for i in range(1, n):
        if nines:
            r[i] = 9
        elif r[i] < r[i-1]:
            sub1(r, i-1)
            r[i] = 9
            nines = True
    #print r
    res = ""
    skip0 = True
    for k in r:
        if k == 0 and skip0:
            pass
        else:
            res += str(k)
            skip0 = False
    return res

tests = int(raw_input())
for k in range(tests):
    s = raw_input()
    x = solve(s)
    print "Case #%d: %s" % (k+1, x)
