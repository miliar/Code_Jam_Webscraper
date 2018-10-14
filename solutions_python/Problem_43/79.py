#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) DDPAlphaTiger1 2009
# Will be under GPL after the end of GCJ
# Under no-use-by-anyone-else-than-me license until then :D
# ***** *****
# Thanks for reading my weird code !
# ***** *****
# Note : I have a wiiide screen, that helps ...

import sys

def readline():
    return sys.stdin.readline()[:-1]

def readnlines(n):
    l = []
    for i in range(n):
        l.append(readline())
    return l

def hexabase(c):
    o = ord(c)
    if o <= 57:
        return o - 48
    else:
        return o - 87

for curcase in range(1, int(readline())+1):
    curword = readline()
    l = []
    for c in curword:
        if c not in l: l.append(c)
    base = max(len(l), 2)
    d = {}
    ind = 0
    total = 0
    for c in curword:
        if not d.has_key(c):
            if ind == 0:
                d[c] = 1
            elif ind == 1:
                d[c] = 0
            else:
                d[c] = ind
            ind += 1
        total = total * base + d[c]
    print "Case #%d: %d" % (curcase, total)
