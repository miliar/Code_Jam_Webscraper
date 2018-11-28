#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def solve(A, B):
    base = 10
    while base <= A:
        base *= 10
    assert base > A and base > B
    recycled = set()
    for num in xrange(A, B+1):
        low = 10
        high = base / low
        while high >= 10:
            if num % low >= low / 10:
                changed = high * (num % low) + num / low
                if A <= num < changed <= B:
                    recycled.add((num, changed))
            low *= 10
            high /= 10
    return len(recycled)

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    A, B = map(int, line.strip().split())
    print 'Case #{i}: {res}'.format(i=i, res=solve(A, B))
