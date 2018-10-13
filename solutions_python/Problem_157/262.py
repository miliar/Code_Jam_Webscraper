#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# c.durr - google code jam - 2015
# Dijkstra
# https://code.google.com/codejam/contest/6224486/dashboard#s=p2
#
# Y = chaîne d'entrée de longueur L
# On commence par décider si Y^X se réduit à -1 (comme ijk), sinon on rejette
# puis on cherche le plus préfixe qui se réduit à i
# et à partir de la le plus court préfixe qui se réduit à j
# comme Z^4 = 1 pour tout Z ...

import sys;

from sys       import *

def readstr():    return stdin.readline().strip()
def readint():    return int(stdin.readline())
def readarray(f): return list(map(f, stdin.readline().split()))

ONE = 0
I   = 1
J   = 2
K   = 3
NEG = 4
NI  = 5
NJ  = 6
NK  = 7

Q = [[ONE,   I,   J,   K, NEG,  NI,  NJ,  NK],
     [  I, NEG,   K,  NJ,  NI, ONE,  NK,   J],
     [  J,  NK, NEG,   I,  NJ,   K, ONE,  NI],
     [  K,   J,  NI, NEG,  NK,  NJ,   I, ONE],
     [NEG,  NI,  NJ,  NK, ONE,   I,   J,   K],
     [ NI, ONE,  NK,   J,   I, NEG,   K,  NJ],
     [ NJ,   K, ONE,  NI,   J,  NK, NEG,   I],
     [ NK,  NJ,   I, ONE,   K,   J,  NI, NEG]]

def mult(y):
    res = ONE
    first = [-1]*8
    for i in range(len(y)):
        res = Q[res][y[i]]
        if first[res] == -1:
            first[res] = i
    return (res, first)

def solve(y, x):
    if mult(y*(x%4))[0] != NEG:
        return False
    first = mult(y*min(4,x))[1]
    a = first[I]
    if a==-1:
        return False
    L = len(y)
    a += 1
    if a%L==0:
        first = mult(y*min(4,x-a//L))[1]
    else:
        first = mult(y[a%L:] + y*min(4, x-a//L-1) )[1]
    return first[J] != -1

for idxCase in range(readint()):
    L,x = readarray(int)
    y   = list(map(lambda z: ord(z)-ord('i')+1, readstr()))
    ANS = ["NO", "YES"]
    print ("Case #%d: %s" % (idxCase+1, ("YES" if solve(y,x) else "NO")))
