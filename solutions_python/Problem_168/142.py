#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, math, random, operator
from string import ascii_lowercase
from string import ascii_uppercase
from fractions import Fraction, gcd
from decimal import Decimal, getcontext
from itertools import product, permutations, combinations
from Queue import Queue, PriorityQueue
from collections import deque, defaultdict, Counter
from bisect import bisect_left
getcontext().prec = 100

MOD = 10**9 + 7
INF = float("+inf")

if sys.subversion[0] != "CPython":  # PyPy?
    raw_input = lambda: sys.stdin.readline().rstrip()
pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")

read_str = raw_input
read_strs = lambda: raw_input().split()
read_int = lambda: int(raw_input())
read_ints = lambda: map(int, raw_input().split())
read_float = lambda: float(raw_input())
read_floats = lambda: map(float, raw_input().split())

"---------------------------------------------------------------"


def solve(R, C):
    M = {}
    rows = {y: list() for y in xrange(R)}
    cols = {x: list() for x in xrange(C)}
    tocheck = list()
    for y in xrange(R):
        s = read_str()
        for x, v in enumerate(s):
            M[x, y] = v
            if v != ".":
                rows[y].append(x)
                cols[x].append(y)
                tocheck.append((x, y))

    for y in xrange(R):
        rows[y].sort()
    for x in xrange(C):
        cols[x].sort()

    ans = 0
    for x, y in tocheck:
        v = M[x, y]
        if v == ">":
            line = rows[y]
            index = bisect_left(line, x) + 1
            sz = len(line)
        elif v == "<":
            line = rows[y]
            index = bisect_left(line, x) - 1
            sz = len(line)
        elif v == "^":
            line = cols[x]
            index = bisect_left(line, y) - 1
            sz = len(line)
        elif v == "v":
            line = cols[x]
            index = bisect_left(line, y) + 1
            sz = len(line)
        else:
            assert 0

        # print "  CHK", x, y, ":", index, line
        if index < 0 or index >= sz:
            # print "  BAD"
            if len(line) > 1:
                ans += 1
            elif len(cols[x]) > 1:
                ans += 1
            elif len(rows[y]) > 1:
                ans += 1
            else:
                return "IMPOSSIBLE"
    return ans


t = read_int()
for i in xrange(t):
    r, c = read_ints()
    res = solve(r, c)
    print "Case #%d: %s" % (i + 1, res)
