from __future__ import division
import sys
import math
import collections

t = int(sys.stdin.readline())
for t0 in range(t):
    n, k = sys.stdin.readline().split(' ')
    n, k = int(n), int(k)
    u = float(sys.stdin.readline().strip())

    p = list(map(float, sys.stdin.readline().split(' ')))
    p = sorted(p)
    d = {}

    for prob in p:
        try:
            d[prob] += 1
        except:
            d[prob] = 1

    keys  = sorted(d.keys())

    while keys and u > 10e-14:
        curr = keys[0]
        keys = keys[1:]
        if not keys:
            new = curr + u/d[curr]
            d[new] = d[curr]
            d.pop(curr)
        else:
            if u >= (keys[0] - curr) * d[curr]:
                u -=  (keys[0] - curr) * d[curr]
                d[keys[0]] += d[curr]
                d.pop(curr)
            else:
                new = curr + u/d[curr]
                d[new] = d[curr]
                d.pop(curr)
                u = 0
    res = 1
    for x in d.items():
        res *= x[0] ** x[1]

    print("Case #", t0 + 1, ": ", min(1,res), sep = '')