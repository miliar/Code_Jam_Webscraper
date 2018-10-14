#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
from operator import mul

def f(N, U, Q):
    lo, hi = 0.0, 1.0
    for _ in xrange(100):
        P = Q[:]
        x = (lo + hi) / 2.
        avail = U
        for i in xrange(N):
            if P[i] < x:
                avail -= (x - P[i])
                P[i] = x
        if avail < 0:
            hi = x
        else:
            lo = x
    return reduce(mul, P)


T = int(raw_input())
for loop in xrange(T):
    N, K = map(int, raw_input().split())
    assert N == K
    U = float(raw_input())
    P = map(float, raw_input().split())
    res = f(N, U, P)
    print 'Case #{}: {:.15f}'.format(loop+1, res)
