#!/usr/bin/python

from sys import stdin
from itertools import product

def calc(N, M, table):
    table_t    = zip(*table)
    horizontal = [max(row) for row in table]
    vertical   = [max(row) for row in table_t]
    for y, x in product(range(N), range(M)):
        if table[y][x] < min(horizontal[y], vertical[x]):
            return 'NO'
    return 'YES'

T = int(stdin.readline())
for i in range(T):
    N, M = map(int, stdin.readline().split())
    table = [map(int, list(stdin.readline().strip().split())) for j in range(N)]
    print "Case #%d: %s" % (i + 1, calc(N, M, table))
