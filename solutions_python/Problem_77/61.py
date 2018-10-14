#!/usr/bin/env python

import sys
import math

l = []
v = []

def visita(i):
    if v[i]:
        return 0
    v[i] = True
    if l[i] == i:
        return 1
    else:
        return visita(l[i]) + 1

sys.setrecursionlimit(2000)

C = int(sys.stdin.readline())
for xxx in xrange(C):
    sys.stdin.readline()
    l = [int(x) - 1 for x in sys.stdin.readline().split()]
    v = [False for x in l]
    E = 0
    for i in xrange(len(l)):
        if not v[i] and l[i] != i:
            ciclo = visita(i)
            E += ciclo



    print "Case #" + str(xxx+1) + ": %.6lf" % E




