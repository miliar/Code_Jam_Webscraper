#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# c.durr - google code jam - 2015
# Infinite House of Pancakes
# https://code.google.com/codejam/contest/6224486/dashboard#s=p1
#
# on utilise s minutes spéciales au début pour distribuer les plus 
# grosses piles sur des plats vides, tel qu'aucune pile ne dépasse t-s.
# pour déterminer si on peut finir en t minutes on testes tous les valeurs pour s
# finalement on détermine le temps optimal par recherche dichotomique

import sys;

from sys       import *

def readstr():    return stdin.readline().strip()
def readint():    return int(stdin.readline())
def readarray(f): return list(map(f, stdin.readline().split()))

def specialmin(p, h):
    s = 0
    for pi in p:
        if pi % h == 0:
            s += pi//h - 1
        else:
            s += pi//h 
    return s

def can_make(p, t):
    for s in range(t):
        if specialmin(p, t-s)<=s:
            return True
    return False

def solve(p):
    lo = 1
    hi = max(p)
    while lo<hi:
        m = (hi+lo)//2
        if can_make(p, m):
            hi = m
        else:
            lo = m+1
    return hi

for idxCase in range(readint()):
    D = readint()
    p = readarray(int)
    print ("Case #%d: %d" % (idxCase+1, solve(p)))
