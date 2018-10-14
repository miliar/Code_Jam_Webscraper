#!/usr/bin/python3

import sys
from fractions import Fraction

t = int(sys.stdin.readline())

def parse_float(s):
    a, b = [int(x) for x in s.split('.')]
    return a * 10000 + b

def solve(n, v, x, l):
    if len(l) == 1:
        r, c = l[0]
        if c != x:
            return None
        return Fraction(v, r)
    if len(l) == 2:
        r1, c1 = l[0]
        r2, c2 = l[1]
        if x < min(c1, c2):
            return None
        if x > max(c1, c2):
            return None
        if c1 == x:
            return Fraction(v, r1)
        if c2 == x:
            return Fraction(v, r2)
        t2 = Fraction(v * c1 - v*x, c1*r2 - c2*r2)
        t1 = (Fraction(v) - Fraction(r2)*t2) / r1
        return max(t1, t2)
    raise NotImplementedError('wtf?')

for i in range(1, t+1):
    n, v, x = sys.stdin.readline().split()
    n = int(n)
    v = parse_float(v)
    x = parse_float(x)
    l = {}
    for j in range(1, n+1):
        r, c = sys.stdin.readline().split()
        r = parse_float(r)
        c = parse_float(c)
        l[c] = l.get(c, 0) + r
    l = [(r, c) for c, r in l.items()]
    sol = solve(n, v, x, l)
    if sol is None:
        print('Case #{0}: IMPOSSIBLE'.format(i))
    else:
        print('Case #{0}: {1}'.format(i, float(sol)))