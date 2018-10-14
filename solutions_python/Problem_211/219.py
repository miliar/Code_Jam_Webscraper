#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from functools import reduce
from operator import mul

def read_ints():
    return [int(''.join(ch for ch in p if ch != '.')) for p in input().split()]

def solve(t):
    n, k = read_ints()
    u, = read_ints()
    ps = read_ints()
    ctr = Counter(ps)
    ps = [(c, ctr[c]) for c in sorted(ctr.keys(), reverse=True)]
    ps.insert(0, (10000, 0))
    while 0 < u:
        p, count = ps.pop()
        target, p_count = ps[-1]
        d = target - p
        if d * count < u:
            u -= d*count
            ps[-1] = (target, p_count + count)
        else:
            new = p + u/count
            ps.append((new, count))
            u = 0
    res = reduce(mul, [(p/10000.0)**count for p, count in ps])
    print('Case #{}: {}'.format(t, res))

if __name__ == "__main__":
    for t in range(1, int(input())+1):
        solve(t)
