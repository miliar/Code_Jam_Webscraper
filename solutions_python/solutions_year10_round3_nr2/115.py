#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def cut(b,c,C):
    r = (b*c)**0.5
    return max(b*C,math.floor(r)), math.ceil(r)


def run(a,b,k,C):
    if a*C>=b:
        return k
    p1,p2=cut(a,b,C)
    t1=run(p1,b,k+1,C)
    t2=run(a,p2,k+1,C)
    return min(t1,t2)

N=int(sys.stdin.readline())
for test in range(1,N+1):
    L,P,C = map(int, sys.stdin.readline().split())
    result = 0
    result = run(L,P,0,C)
    
    print "Case #%d: %d" % (test, result)
    
