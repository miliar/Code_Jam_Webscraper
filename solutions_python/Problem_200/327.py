#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

name = "B-large"
path = "data/qb/"

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")


def solve(s):
    if s < 10:
        return s

    l = [int(c) for c in list(str(s))]
    L = len(l)
    for i in reversed(xrange(1, L)):
        if l[i] >= l[i - 1]:
            continue

        l[i - 1] -= 1
        for j in xrange(i, L):
            l[j] = 9

    return int(''.join([str(c) for c in l]))


testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input()

    res = solve(line)

    if res is False:
        print "Case #" + str(testCase) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(testCase) + ": " + ("%d" % res)
