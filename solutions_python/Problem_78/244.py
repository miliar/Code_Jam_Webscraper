#!/usr/bin/env python

import os
import sys

t = int(sys.stdin.readline())

def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)

for test in range(t):
    n,pd,pg = [int(x) for x in sys.stdin.readline().split()]
    good = True
    if n < 100/gcd(100,pd):
        good = False
    if pd != 100 and pg == 100:
        good = False
    if pd != 0 and pg == 0:
        good = False

    if good:
        print "Case #%d: Possible" % (test+1)
    else:
        print "Case #%d: Broken" % (test+1)
