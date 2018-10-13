#!/usr/bin/env python2.7
from __future__ import print_function
from fractions import gcd

def lcm(a, b):
    d = gcd(a,b)
    return (a * b) / d

def read_case():
    N, L, H = map(int, raw_input().split())
    freqs = map(int, raw_input().split())
    return (N, L, H, freqs)

def solve(case):
    N, L, H, freqs = case
    for f in xrange(L, H+1):
        failed = False
        for f2 in freqs:
            if f2 % f != 0 and f % f2 != 0:
                failed = True
                break
        if not failed:
            break
    return "NO" if failed else f

T = int(raw_input())
for caseidx in xrange(1, T+1):
    print("Case #{}: {}".format(caseidx, solve(read_case())))
