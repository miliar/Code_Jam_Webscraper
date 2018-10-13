#!/usr/bin/env python

from sys import stdin
from math import ceil
from gmpy import comb

T = int(stdin.readline())

mem = {}

def pure(n, rank):
    answer = 0

    if rank == 1:
        return 1

    if (n, rank) in mem:
        return mem[(n, rank)]

    for i in xrange(1,rank):
        answer += pure(rank, i)*int(comb(n-rank-1, rank-i-1))

    mem[(n,rank)] = answer
    return answer

for CASO in xrange(1,T+1):
    (n, ) = [int(x) for x in stdin.readline().strip().split(" ")]

    answer = 0

    for i in xrange(1,n):
        answer += pure(n, i)

    print "Case #%d: %d" % (CASO, answer % 100003)
