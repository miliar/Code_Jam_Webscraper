#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# c.durr - google code jam - 2015
# Ominous Omino
# https://code.google.com/codejam/contest/6224486/dashboard#s=p3
#

import sys;

from sys       import *

def readstr():    return stdin.readline().strip()
def readint():    return int(stdin.readline())
def readarray(f): return list(map(f, stdin.readline().split()))

def solve(x, r, c):
    if r>c:
        r,c = c,r
    S = (x+1)//2 # smallest leg of L-shape
    L = x-S+1    # longer leg
    if (r*c)%x != 0 or r < S or (r == S and c < L) or x >= 7:
        return True
    if r > S:
        return False
    # now r==S and c>=L
    for a in range(x-r+1):
        ok = False
        for b in range(a,min(c-x+r+a, c)):
            if (r*b)%x == a:
                ok = True
                break
        if not ok:
            return True
    return False

for idxCase in range(readint()):
    x,r,c = readarray(int)
    print ("Case #%d: %s" % (idxCase+1, ("RICHARD" if solve(x,r,c) else "GABRIEL")))
