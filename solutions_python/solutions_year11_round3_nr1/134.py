#!/usr/bin/env python

from sys import stdin

T = int(stdin.readline())

dirs = [(0,1),(1,0),(1,1)]
repl = ['\\', '\\', '/']

def f(R, C, P):
    for i in xrange(R):
        for j in xrange(C):
            if P[i][j] == "#":
                P[i][j] = '/'

                for dd in xrange(3):
                    (ni, nj) = (i+dirs[dd][0],j+dirs[dd][1])

                    if ni >= R or nj >= C:
                        return None

                    if P[ni][nj] != '#':
                        return None

                    P[ni][nj] = repl[dd]

    return P


for CASO in xrange(1,T+1):
    (R, C) = [int(x) for x in stdin.readline().strip().split(" ")]

    P = []

    for i in xrange(R):
        row = []
        s = stdin.readline().strip()

        for c in s:
            row.append(c)

        P.append(row)

    result = f(R, C, P)

    print "Case #%d:" % CASO

    if result:
        for row in result:
            print "".join(row)
    else:
        print "Impossible"
