#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    N, P = map(int, fin.readline().split())
    groups = map(int, fin.readline().split())
    r = [0] * P
    for g in groups:
        r[g % P] += 1
    # debug(r)

    result = 0
    if P == 2:
        result = r[0] + (r[1] + 1) // 2
    elif P == 3:
        result = r[0]
        k = min(r[1], r[2])
        result += k
        r[1] -= k
        r[2] -= k
        result += r[1] // 3
        r[1] %= 3
        result += r[2] // 3
        r[2] %= 3
        if r[1] > 0 or r[2] > 0:
            result += 1
    elif P == 4:
        result = r[0]
        k = min(r[1], r[3])
        result += k
        r[1] -= k
        r[3] -= k
        twos = r[2] + r[1]//2 + r[3]//2
        r[1] %= 2
        r[3] %= 2
        result += twos // 2
        twos %= 2
        remaining = twos + r[1] + r[3]
        if remaining > 0:
            result += 1

    print("Case #%d: %s" % (case, result))

