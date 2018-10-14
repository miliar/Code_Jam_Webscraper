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
    data = readline().split()
    time = 0
    timeb = 0
    timeo = 0
    blue = 1
    oran = 1
    for i in range(1, int(data[0])+1):
        if data[2*i-1] == 'B':
            newpos = int(data[2*i])
            time += max(0, abs(blue - newpos) - (time - timeb)) + 1
            timeb = time
            blue = newpos
        else:
            newpos = int(data[2*i])
            time += max(0, abs(oran - newpos) - (time - timeo)) + 1
            timeo = time
            oran = newpos
    print "Case #%d: %d" % (curcase, time)
