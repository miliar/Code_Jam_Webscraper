#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) DDPAlphaTiger1 2011
# Will be under GPL after the end of GCJ
# Under no-use-by-anyone-else-than-me license until then :D
# ***** *****
# Thanks for reading my weird code !
# ***** *****
# Note : I have a wiiide screen, that helps ...

import sys

import psyco
psyco.full()

globrep = {}
globopp = {}
globseq = []
globcuropp = []

def readline():
    return sys.stdin.readline()[:-1]

def readnlines(n):
    l = []
    for i in range(n):
        l.append(readline())
    return l

def getlist(d, x):
    if d.has_key(x):
        return d[x]
    else:
        return []

def invoke(c):
    global globseq
    global globrep
    global globcuropp
    global globopp
    if len(globseq) > 0:
        if globrep.has_key((globseq[-1], c)):
            newc = globrep[(globseq[-1], c)]
            if globseq[-1] not in globseq[:-1]:
                globcuropp = []
                map(lambda x: globcuropp.extend(getlist(globopp, x)), globseq[:-1])
            globseq = globseq[:-1]
            invoke(newc)
        elif c in globcuropp:
            globseq = []
            globcuropp = []
        else:
            globseq.append(c)
            globcuropp.extend(getlist(globopp, c))
    else:
        globseq.append(c)
        globcuropp.extend(getlist(globopp, c))

for curcase in range(1, int(readline())+1):
    data = readline().split()
    globrep = {}
    globopp = {}
    globseq = []
    globcuropp = []
    nbrep = int(data[0])
    for i in range(1, 1 + nbrep):
        currep = data[i]
        globrep[(currep[0], currep[1])] = currep[2]
        globrep[(currep[1], currep[0])] = currep[2]
    nbopp = int(data[nbrep+1])
    for i in range(2 + nbrep, 2 + nbrep + nbopp):
        curopp = data[i]
        if globopp.has_key(curopp[0]):
            globopp[curopp[0]].append(curopp[1])
        else:
            globopp[curopp[0]] = [curopp[1]]
        if globopp.has_key(curopp[1]):
            globopp[curopp[1]].append(curopp[0])
        else:
            globopp[curopp[1]] = [curopp[0]]
    seq = data[3 + nbrep + nbopp]
    for x in seq:
        invoke(x)
    print "Case #%d: [%s]" % (curcase, ', '.join(globseq))
