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

existing = {}

def readline():
    return sys.stdin.readline()[:-1]

def readnlines(n):
    l = []
    for i in range(n):
        l.append(readline())
    return l

def addpath(existing, path):
    if len(path) == 0:
        return 0
    cur = path[0]
    if existing.has_key(cur):
        return addpath(existing[cur], path[1:])
    else:
        existing[cur] = {}
        return 1+addpath(existing[cur], path[1:])

for curcase in range(1, int(readline())+1):
    [n, m] = map(int, readline().split())
    existing = {}
    map(lambda p: addpath(existing, p.split('/')[1:]), readnlines(n))

    print "Case #%d: %d" % (curcase, sum(map(lambda p: addpath(existing, p.split('/')[1:]), readnlines(m))))
