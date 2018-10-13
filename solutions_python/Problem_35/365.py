#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys       import stdin, stdout
from itertools import izip

T = int(stdin.readline().strip())

def getElevation(emap, x, y, W, H):
    if x < 0 or y < 0 or y >= len(emap) or x >= len(emap[0]):
        return 99999
    return emap[y][x]

def followDown(emap, x, y, W, H, sinks):
    if sinks[y][x] != None:
        return sinks[y][x]

    n = getElevation(emap, x, y-1, W, H)
    s = getElevation(emap, x, y+1, W, H)
    e = getElevation(emap, x+1, y, W, H)
    w = getElevation(emap, x-1, y, W, H)
    m = min(n,s,e,w)

    if emap[y][x] <= m:
        sinks[y][x] = (x,y)
        return (x,y)

    if n == m:
        sinks[y][x] = followDown(emap, x, y-1, W, H, sinks)
    elif w == m:
        sinks[y][x] = followDown(emap, x-1, y, W, H, sinks)
    elif e == m:
        sinks[y][x] = followDown(emap, x+1, y, W, H, sinks)
    elif s == m:
        sinks[y][x] = followDown(emap, x, y+1, W, H, sinks)
    return sinks[y][x]

for case in xrange(T):
    H, W   = map(int, stdin.readline().split())
    emap   = []
    sinks  = []
    basins = {}
    nextchar = ord("a")

    for y in xrange(H):
        emap.append(map(int, stdin.readline().split()))
        sinks.append([None] * W)

    for y in xrange(H):
        for x in xrange(W):
            sinks[y][x] = followDown(emap, x, y, W, H, sinks)

    print "Case #%d:" % (case+1,)

    for y in xrange(H):
        row = []
        for x in xrange(W):
            if not sinks[y][x] in basins:
                basins[sinks[y][x]] = chr(nextchar)
                nextchar += 1
            row.append(basins[sinks[y][x]])
        print " ".join(row)
