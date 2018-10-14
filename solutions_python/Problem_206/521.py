#!/usr/bin/python

from collections import deque

def ir():
    return int(raw_input())

def ia():
    line = raw_input()
    line = line.split()
    return map(int, line)

# [......K1...K2...]
# 
# 

def solve():
    D, N = ia()
    H = [ ]
    for i in xrange(N):
        k, s = ia()
        dst = D - k
        spd = s
        H.append( (dst, spd) )

    H.sort()
    sp = []
    for dst, spd in H:
        if dst == 0: continue
        csp = spd * D / float(dst)
        sp.append(csp)

    return min(sp)

T = ir()
for it in xrange(1, T + 1):
    ans = solve()
    print "Case #%d:" % it, ans
