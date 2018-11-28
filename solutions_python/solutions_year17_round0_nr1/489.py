#!/bin/env python

# google code jam 2017 qualifiers problem 1
# Daniel Scharstein

import sys

def solve(a, n):
    #print a, n
    k = 0
    for i in range(len(a)-n+1):
        if not a[i]:
            for j in range(i, i+n):
                a[j] = not a[j]
            #print a
            k += 1
    if all(a[-n:]):
        return k
    return "IMPOSSIBLE"

tests = int(raw_input())
for k in range(tests):
    s, n = raw_input().split()
    n = int(n)
    a = [x == '+' for x in s]
    x = solve(a, n)
    print "Case #%d: %s" % (k+1, x)
