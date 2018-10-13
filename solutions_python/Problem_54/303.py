#!/usr/bin/env python

from sys import stdin
from fractions import gcd

C = int(stdin.readline())

def falta(a, M):
    return (M-(a%M))%M

for CASO in xrange(1,C+1):
    line = [int(x) for x in stdin.readline().split(" ")]
    N = line[0]
    T = line[1:]

    T.sort(reverse=True)
    S = set()

    for i in xrange(N):
        for j in xrange(i+1,N):
            S.add(T[i]-T[j])

    M=T[0]-T[1]

    for i in S:
        M=gcd(M,i)

    print "Case #%d: %d" % (CASO, (M-(T[0]%M))%M)
