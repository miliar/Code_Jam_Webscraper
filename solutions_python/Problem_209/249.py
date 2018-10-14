#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import *
from itertools import *
from math import pi

def read_ints():
    return list(map(int, input().split()))

def area(r, h):
    return side(r, h) + pi*r*r

def side(r, h):
    return h * 2 * pi * r

def wat(ps):
    first = max(ps, key=lambda p: p[0])
    ps.remove(first)
    ps.sort(key=lambda p: side(*p), reverse=True)
    return area(*first) + sum(side(r, h) for r, h in ps[:k-1])
    return top + sum(side(r, h) for r, h in xs)

def wut(ps):
    first = max(ps, key=lambda p: area(*p))
    ps.remove(first)
    ps.sort(key=lambda p: side(*p), reverse=True)
    xs = [first]
    xs.extend(ps[:k-1])
    top = pi * max(r for r, _ in xs)**2
    return top + sum(side(r, h) for r, h in xs)
    
def solve(t):
    global k
    N, k = read_ints()
    ps = [tuple(read_ints()) for _ in range(N)]
    print('Case #{}: {}'.format(t, max(wat(ps.copy()), wut(ps.copy()))))

if __name__ == "__main__":
    for t in range(1, int(input())+1):
        solve(t)
