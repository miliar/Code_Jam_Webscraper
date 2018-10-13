#!/usr/bin/env python

from fractions import gcd
from sys import stdin
from math import ceil

t = input()

for test in range(t):
    n, pd, pg = [int(i) for i in stdin.readline().strip().split()]
    
    gamesd = 100/gcd(100, pd)
    
    possible = False
    if gamesd <= n:
        possible = True
    if pg == 100:
        if pd != 100:
            possible = False
    if pg == 0:
        if pd != 0:
            possible = False

    print "Case #%d: %s" % (test+1, "Possible" if possible else "Broken")