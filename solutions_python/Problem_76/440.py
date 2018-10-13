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

for curcase in range(1, int(readline())+1):
    ignore = readline()
    data = map(int, readline().split())
    data.sort()
    resxor = data[0]
    ressum = 0
    for x in data[1:]:
        resxor = resxor ^ x
        ressum += x
    print "Case #%d: %s" % (curcase, str(ressum) if (resxor == 0) else "NO")
