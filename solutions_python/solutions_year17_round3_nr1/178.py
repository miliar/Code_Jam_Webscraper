#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from math import pi

def max_side_area(RHs, start, end, k):
    rhs = sorted([RHs[i][0]*RHs[i][1] for i in range(start, end)], reverse = True)
#    print rhs
    return sum(rhs[:k])    

def solve(N, K, RHs):
#    print RHs
    max_area = 0
    for i in range(N-K+1):
        r, h = RHs[i]
        rh = r*h
        rh += max_side_area(RHs, i+1, N, K-1)
        a = r*r + 2*rh
        if a > max_area:
#            print r, h, rh, a
            max_area = a
        
    return max_area

T = int(raw_input())

for test_case in range(1, T+1):
    N, K = [int(s) for s in raw_input().split(" ")]
    RHs = [[int(s) for s in raw_input().split(" ")] for i in range(N)]
#    print B, M
    solution = solve(N, K, sorted(RHs, key=lambda rh: rh[0], reverse = True))
    print "Case #{}: {}".format(test_case, pi*solution)
