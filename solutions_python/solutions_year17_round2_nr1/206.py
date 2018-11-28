#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_ints():
    return list(map(int, input().split()))

def solve(t):
    D, n = read_ints()
    hs = [read_ints() for _ in range(n)]
    x = max((D - d) / speed for d, speed in hs)
    print('Case #{}: {}'.format(t, D/x))

if __name__ == "__main__":
    for t in range(1, int(input())+1):
        solve(t)
