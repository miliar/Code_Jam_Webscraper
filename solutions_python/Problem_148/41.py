#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    N, X = map(int, fin.readline().split())
    sizes = list(map(int, fin.readline().split()))
    sizes.sort()
    a = 0
    b = N - 1
    discs = 0
    while b > a:
        large = sizes[b]
        small = sizes[a]
        if large + small <= X:
            b -= 1
            a += 1
            discs += 1
        else:
            b -= 1
            discs += 1
    if b == a:
        discs += 1

    print("Case #%d: %s" % (case, discs))