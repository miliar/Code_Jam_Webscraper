#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import xor

def f(c):
    if reduce(xor, c):
        return 'NO'
    return sum(c) - min(c)

t = int(raw_input())
for case in range(1, t+1):
    _ = raw_input()
    c = [int(c) for c in raw_input().split()]
    res = f(c)
    print 'Case #{0}: {1}'.format(case, res)

