#!/usr/bin/env python3

import sys

cases = int (input ())

def lmin (l):
    min = l [0]
    for i in l:
        if i < min:
            min = i

    return min

def lmax (l):
    max = l [0]
    for i in l:
        if i > max:
            max = i

    return max

def allSame (l):
    n = l [0]
    for i in l:
        if i != n:
            return False

    return True

def _solve (g):
    for row in g:
        if not allSame (row):
            m = lmax (row)
            for col in range (len (row)):
                if row [col] != m:
                    if not allSame ([g [i][col] for i in range (len(g))]):
                        return False

    return True

def transpose (g):
    gT = [[] for i in g[0]]

    for row in g:
        i = 0
        for e in gT:
            e.append (row [i])
            i = i + 1

    print ("Transpose of {0} is {1}".format (str (g).replace ("]", "]\n"),
    str (gT).replace ("]", "]\n")), file=sys.stderr)

    return gT

def solve (g):
    if not _solve (g):
        return _solve (transpose (g))

    transpose (g)
    return True

def answer ():
    dimensions = input ().split ()

    width = int (dimensions [1])
    length = int (dimensions [0])

    grass = []

    for i in range (length):
        grass.append ([int (e) for e in input ().split ()])

    # print ("The lawn is {0}".format (grass), file=sys.stderr)

    return "YES" if solve (grass) else "NO"

for i in range (cases):
    print ("Case #{0}: {1}".format (i + 1, answer ()))
