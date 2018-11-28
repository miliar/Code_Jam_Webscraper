#!/usr/bin/python
from __future__ import print_function
from sys import stdin
#log = open("C:\\Users\\tx_2\Documents\\Coding\\Google Code Jam 2015\\D-small-output.txt", "w")

def readiline():
    return map( int, stdin.readline().strip().split() )

def readsline():
    return map( str, stdin.readline().strip().split() )

T, = readiline()

for i in xrange(1,T+1):
    X,R,C = readiline()
    if X == 1:
        winguarantee = True
    else:
        winguarantee = True
        if (R <= X-2) or (C<= X-2):
            winguarantee = False
        if (R <= X-1) and (C<=X-1):
            winguarantee = False
        if R*C%X != 0:
            winguarantee = False

    if winguarantee:
        print ('Case #%d: GABRIEL' % (i))
    else:
        print ('Case #%d: RICHARD' % (i))
