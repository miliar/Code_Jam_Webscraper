#!/usr/bin/env python

from sys import stdin

T = int(stdin.readline())

def case(N, S, p, t):
    normal = 0
    surprising = 0

    for x in t:
        n, s = False, False

        for i in xrange(0, 11):
            for j in xrange(0, 11):
                for k in xrange(0, 11):
                    if i+j+k != x:
                        continue

                    if i < p and j < p and k < p:
                        continue

                    if max([i,j,k]) - min([i,j,k]) > 2:
                        continue

                    if abs(i-j) <= 1 and abs(i-k) <= 1 and abs(j-k) <= 1:
                        n = True
                    else:
                        s = True

        if n:
            normal += 1
        elif s:
            surprising += 1

    return normal + min(surprising, S)

for CASE in xrange(1,T+1):
    l = [int(x) for x in stdin.readline().strip().split(" ")]
    N, S, p, t = l[0], l[1], l[2], l[3:]

    print "Case #%d: %d" % (CASE, case(N, S, p, t))
