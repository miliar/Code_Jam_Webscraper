#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=975485#s=p2
'''

import sys, re, math

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]

ncases = ints()[0]
for casenum in range(ncases):
    N = ints()[0]
    cs = sorted(ints())
    x = 0
    for c in cs: x^=c
    if x:
        print "Case #%d: NO" % (casenum+1)
        continue
    print "Case #%d: %d" % (casenum+1, sum(cs)-cs[0])
    
