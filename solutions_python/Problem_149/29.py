#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    #debug("Case #%d" % case)

    N = int(fin.readline())
    numbers = list(map(int, fin.readline().split()))

    ordered = numbers[:]
    ordered.sort()
    index = {}
    for i, n in enumerate(numbers):
        index[n] = i

    steps = 0
    for j, n in enumerate(ordered):
        i = numbers.index(n)
        l = i
        r = len(numbers)-i-1
        steps += min(l, r)
        del numbers[i]




    print("Case #%d: %s" % (case, steps))

# 98 3986 2708 468 4907 5915 657 257 8714

# 98 3986 2708 468 4907 5915 8714 657 257
# 98 468 2708 3986 4907 5915 8714 657 257


# 98 468 2708 3986 4907 5915 8714 2657 57


# 98 3986 2708 468 4907 5915 657 257 8714
# 98 2708 468 3986 4907 5915 657 8714 257
# 98 468 2708 3986 4907 5915 8714 657 257