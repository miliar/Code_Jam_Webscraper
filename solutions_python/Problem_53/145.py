# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=433101#s=p0
'''

import sys, re

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]

T = int(lin())

for casenum in range(T):
    (N,K) = ints()
    print "Case #%d: %s" % (casenum+1, 'ON' if K%(2**N)==(2**N-1) else 'OFF')
