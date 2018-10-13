#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from bisect import bisect_left, bisect_right

# precomputed sqrt's of Fair and Square for [1; 10**14]

FSQRT = [
    1,
    2,
    3,
    11,
    22,
    101,
    111,
    121,
    202,
    212,
    1001,
    1111,
    2002,
    10001,
    10101,
    10201,
    11011,
    11111,
    11211,
    20002,
    20102,
    100001,
    101101,
    110011,
    111111,
    200002,
    1000001,
    1001001,
    1002001,
    1010101,
    1011101,
    1012101,
    1100011,
    1101011,
    1102011,
    1110111,
    1111111,
    2000002,
    2001002,
]

FS = [n * n for n in FSQRT]


def solve(A, B):
    N = len(FS)
    ia = bisect_left(FS, A)
    if ia == N:
        return 0
    ib = bisect_right(FS, B)
    if ib == 0:
        return 0
    assert ia <= ib
    return ib - ia


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


T = int(ifs.readline())
for t in range(1, T + 1):
    A, B = numbers_from_line()
    a = solve(A, B)
    ofs.write('Case #%d: %d\n' % (t, a))
