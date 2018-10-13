#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

name = "C-large"
path = "data/qc/"

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")


def k_iter(n):
    d = defaultdict(int)
    d[n] += 1

    while True:
        pick = max(d.keys())
        c = d.pop(pick)
        x = pick / 2

        if pick % 2 == 1 or pick == 0:
            yield (x, x), c
            d[x] += 2 * c
        else:
            yield (x, x - 1), c
            d[x] += c
            d[x - 1] += c


def solve(n, k):
    s = 0
    for (a, b), c in k_iter(n):
        #print a, b, c, s
        s += c
        if s >= k:
            return (a, b)


testCases = int(input())

for testCase in range(1, testCases + 1):
    line = raw_input().split(" ")
    N = int(line[0])
    K = int(line[1])

    res = solve(N, K)

    if res is False:
        print "Case #" + str(testCase) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(testCase) + ": " + ("%d %d" % res)
