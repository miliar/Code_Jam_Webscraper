# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=433101#s=p1
'''

import sys

def abs(x): return x if x>=0 else -x

def gcd(a, b):
    if b==0: return abs(a)
    return gcd(b, a%b)

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]

T = int(lin())

for casenum in range(T):
    ns = ints()
    g = abs(ns[2]-ns[1])
    for i in range(3,len(ns)):
        g = gcd(g, ns[i]-ns[1])
    assert g>0
    ans = 0
    for i in range(1,len(ns)):
        need = 0 if ns[i]%g==0 else g-ns[i]%g
        ans = max(ans, need)
    print "Case #%d: %s" % (casenum+1, ans)
