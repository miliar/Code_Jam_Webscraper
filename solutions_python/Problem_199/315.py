#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

name = "A-large"
path = "data/"

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")


def solve(s, x):
    s = list(s)
    l = len(s)
    c = 0
    for i in xrange(l):
        if s[i] == '+':
            continue

        if l - i < x:
            return False

        for j in xrange(x):
            s[i + j] = '-' if s[i + j] == '+' else '+'

        c += 1
    return c


testCases = int(input())

for testCase in range(1, testCases + 1):
    line = raw_input().split(' ')
    s = line[0]
    x = int(line[1])

    res = solve(s, x)
    if res is False:
        print "Case #" + str(testCase) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(testCase) + ": " + ("%d" % res)
