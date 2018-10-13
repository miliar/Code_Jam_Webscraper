#!/usr/bin/env python3
import sys
from bisect import bisect
from math import floor, ceil

def eprint(*args, **kwargs):
#    print(*args, file=sys.stderr, **kwargs)
    pass

def solve(gaps):
    eprint(gaps)
    gap = gaps.pop()
    left = floor(gap / 2 - 0.5)
    index = bisect(gaps, left)
    gaps[index:index] = [left]
    right = ceil(gap / 2 - 0.5)
    index = bisect(gaps, right)
    gaps[index:index] = [right]
    return (left, right)

t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    gaps = [n]
    dist = (0, 0)

    while k > 0:
        dist = solve(gaps)
        k -= 1

    print("Case #{}: {} {}".format(i, max(dist), min(dist)))
