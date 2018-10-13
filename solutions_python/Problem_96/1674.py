#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

M = {}
cant = 0

def is_surp(t):
    return (max(t) - min(t) == 2)

for a in xrange(0, 11):
    for b in xrange(a, a + 3):
        for c in xrange(a, a + 3):
            t = (a, b, c)
            result = sum(t)
            surp = is_surp(t)

            if not (result in M):
                M[result] = []
            M[result].append(t)

            if surp:
                cant = cant + 1

#print len(M)
#print cant

def buscar(Puntos, P, S):
    n = 0
    idx = 0
    con_surp = [False] * len(Puntos)
    sin_surp = [False] * len(Puntos)
    S_cant = 0

    for x in Puntos:
        for y in M[x]:
            if is_surp(y) and max(y) >= P:
                con_surp[idx] = True
                break
        idx += 1

    idx = 0
    for x in Puntos:
        f = False
        for y in M[x]:
            if max(y) >= P and not is_surp(y):
                n += 1
                sin_surp[idx] = True
                f = True
                break

        if not f:
            if con_surp[idx] and S_cant < S:
                n += 1
                S_cant += 1
        idx += 1

#    print con_surp
#    print sin_surp

    return n

T = int(sys.stdin.readline())

for case_num in xrange(1, T+1):
    line = map(int, sys.stdin.readline().split())
    cant = line[0]
    S = line[1]
    P = line[2]
    Puntos = line[3:]

    print ("Case #%d: %d" % (case_num, buscar(Puntos, P, S)))

