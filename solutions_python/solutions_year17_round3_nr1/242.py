#!/usr/bin/env python
# -*- Encoding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys
import math
import heapq
from collections import defaultdict, deque, namedtuple


sys.setrecursionlimit(1000000)
Pancake = namedtuple('Pancake', 'r h a')

PI = math.pi


def solve(N, K, pancakes, index=0, is_first=True, mem=None):
    if K == 0:
        return 0

    if index >= len(pancakes):
        return None

    key = (K, index, is_first)
    if key in mem:
        return mem[key]

    p = pancakes[index]

    mx = 0
    ans = solve(N, K - 1, pancakes, index + 1, is_first=False, mem=mem)
    if ans is not None:
        mx = p.a + ans
        if is_first:
            mx += PI * p.r ** 2

    ans = solve(N, K, pancakes, index + 1, is_first, mem=mem)
    if ans is not None:
        mx = max(mx, ans)

    mem[key] = mx
    return mx

if __name__ == '__main__':
    T = int(raw_input())
    for Ti in range(T):
        N, K = map(int, raw_input().strip().split(" "))
        pancakes = []
        for Ni in range(N):
            Ri, Hi = map(int, raw_input().strip().split(" "))
            pancakes.append(Pancake(Ri, Hi, 2 * PI * Ri * Hi))
        pancakes.sort(key=lambda x: x.r, reverse=True)
        ans = solve(N, K, pancakes, mem={})
        print("Case #{}: {}".format(Ti + 1, ans))
