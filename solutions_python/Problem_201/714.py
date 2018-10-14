#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache

def read_ints():
    return list(map(int, input().split()))

def divide(n):
    h = n >> 1
    return (n - h, h)

@lru_cache(maxsize=None)
def rec(l, n):
    assert n <= l
    assert 0 < n
    if l == n:
        return (0, 0)
    elif n == 1:
        return divide(l - 1)
    elif n == 2:
        return rec(divide(l - 1)[0], 1)
    else:
        l1, l2 = divide(l - 1)
        n1, n2 = divide(n - 1)
        return min(rec(l1, n1), rec(l2, n2))

def solve(t):
    l, n = read_ints()
    ma, mi = rec(l, n)
    print('Case #{}: {} {}'.format(t, ma, mi))

if __name__ == "__main__":
    for t in range(1, int(input()) + 1):
        solve(t)
