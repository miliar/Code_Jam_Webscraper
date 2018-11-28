#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) DDPAlphaTiger1 2010
# Will be under GPL after the end of GCJ
# Under no-use-by-anyone-else-than-me license until then :D
# ***** *****
# Thanks for reading my weird code !
# ***** *****
# Note : I have a wiiide screen, that helps ...

import sys

import psyco
psyco.full()

def readline():
    return sys.stdin.readline()[:-1]

def readnlines(n):
    l = []
    for i in range(n):
        l.append(readline())
    return l

def mycomp(a,b,c,d):
    if a == c:
        if b == d:
            return 0
        elif b < d:
            return 1
        else:
            return -1
    elif a < c:
        return 1
    else:
        return -1

for curcase in range(1, int(readline())+1):
    [n, k, b, t] = map(int, readline().split())
    xl = map(int, readline().split())
    vl = map(int, readline().split())
    cl = []

    for i in range(0, n):
        cl.append((xl[i], vl[i]))

    cl.sort(lambda (a,b),(c,d): mycomp(a,b,c,d))

    toswap = 0
    todo = k
    total = 0
    for i in range(0, n):
        (x, v) = cl[i]
        if x + v * t >= b:
            total += toswap
            todo -= 1
            if todo == 0:
                break
        else:
            toswap += 1

    if todo == 0:
        print "Case #%d: %d" % (curcase, total)
    else:
        print "Case #%d: IMPOSSIBLE" % (curcase)
