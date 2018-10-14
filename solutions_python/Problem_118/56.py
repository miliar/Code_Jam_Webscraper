#!/usr/bin/env python

import sys

def listOnes(t, l, i, d):
    res = []
    for j in xrange(l, i / 2):
        tj = t + 10 ** j + 10 ** (i - j - 1)
        res.append(tj)
        if d > 0:
            res.extend(listOnes(tj, j + 1, i, d - 1))
    return res

lst = range(4)
for i in xrange(2, 51):
    ones = listOnes(10 ** (i - 1) + 1, 1, i, 2)
    ones.append(10 ** (i - 1) + 1)
    lst.extend(ones)
    lst.append(2 * (10 ** (i - 1)) + 2)
    if i % 2 == 1:
        lst.append(2 * (10 ** (i - 1)) + 10 ** (i / 2) + 2)
        t = 10 ** (i - 1) + 2 * (10 ** (i / 2)) + 1
        lst.append(t)
        for j in xrange(1, i / 2):
            lst.append(t + 10 ** j + 10 ** (i - j - 1))
        for n in ones:
            lst.append(n + 10 ** (i / 2))
lst.sort()
lst = [ n ** 2 for n in lst ]

def count(N):
    l = 0
    u = len(lst)
    while l < u:
        m = (l + u) / 2
        if N < lst[m]:
            u = m
        else:
            l = max(m, l + 1)
    return l

def solve(A, B):
    return str(count(B) - count(A - 1))

def readInts():
    return [ int(s) for s in sys.stdin.readline().split() ]

T = int(sys.stdin.readline())
for t in xrange(T):
    inputs = readInts()
    A = inputs[0]
    B = inputs[1]
    res = solve(A, B)
    print "Case #%d: %s" % (t + 1, res)
