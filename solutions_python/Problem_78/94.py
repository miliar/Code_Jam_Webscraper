#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=1145485#s=p0
'''

import sys, re, math

def gcd(a, b):
    if b==0: return abs(a)
    return gcd(b, a%b)

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]

ncases = ints()[0]
for casenum in range(ncases):
    (N, pD, pG) = ints()
    if pD>100 or pG>100:
        print "Case #%d: Broken" % (casenum+1)
        continue
    gD = gcd(100, pD); hD = 100/gD
    gG = gcd(100, pG); hG = 100/gG
    # hD * kD = D
    # hG * kG = G
    if pG==0 and pD!=0 or pG==100 and pD!=100:
        print "Case #%d: Broken" % (casenum+1)
        continue
    if pD==0:
        print "Case #%d: Possible" % (casenum+1)
        continue
    if hD > N:
        print "Case #%d: Broken" % (casenum+1)
        continue
    print "Case #%d: Possible" % (casenum+1)
    
        
    

    
