# -*- coding: utf-8 -*-

import sys
fin = sys.stdin
T = int(fin.readline())
from bisect import insort

def build_table(dist):
    dp = {}

    for a in xrange(11):
        for b in xrange(11):
            if abs(a - b) > dist:
                continue
            
            for c in xrange(11):
                if abs(c - b) > dist or abs(c - a) > dist:
                    continue
                
                s = a + b + c
                
                l = dp.setdefault(s, [])
                if not a in l:
                    insort(l, a)
                if not b in l:
                    insort(l, b)
                if not c in l:
                    insort(l, c)
    
    return dp

dp = build_table(1)
sdp = build_table(2)

for case in range(1,T+1):   
    vals = fin.readline().split()
    N = int(vals[0])
    S = int(vals[1])
    p = int(vals[2])
    m = 0
    vals = sorted([int(v) for v in vals[3:]])

    for _ in xrange(S):
        for i,v in enumerate(vals):
            if v is None:
                continue
            
            if p > sdp[v][-1]:
                continue
            
            vals[i] = None
            m += 1
            break
                 
    for v in vals:
        if v is None:
            continue
        
        if p > dp[v][-1]:
            continue
         
        m += 1
         
    print "Case #%d: %d" % (case, m)