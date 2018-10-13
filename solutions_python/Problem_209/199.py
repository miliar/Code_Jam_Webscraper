#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
from math import pi

def f(N, K, R, H):
    v = [(R[i], H[i]) for i in xrange(N)]
    v.sort()
    maxi = 0
    for last in xrange(K-1, N):
        r, h = v[last]
        left = v[:last]
        left.sort(key=lambda tup: tup[0] * tup[1], reverse=True)
        left = left[:K-1]
        summ = sum(x * y for x, y in left)
        tmp = r ** 2 + 2 * (summ + r * h)
        maxi = max(maxi, tmp)
    return maxi * pi


T = int(raw_input())

for loop in xrange(T):
    N, K = map(int, raw_input().split())
    R = [0] * N
    H = [0] * N
    for i in xrange(N):
        R[i], H[i] = map(int, raw_input().split())
    res = f(N, K, R, H)
    print 'Case #{}: {:.15f}'.format(loop+1, res)
