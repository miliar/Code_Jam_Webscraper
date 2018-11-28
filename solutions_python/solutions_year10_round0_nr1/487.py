#! /usr/bin/python

import sys

def getline():
    return sys.stdin.readline().strip()

def solve(num):
    n, k = (int(x) for x in getline().split())

    status = 'ON'
    for x in range(n):
        if not (k / (2 ** x) % 2):
            status = 'OFF'
            break

    print 'Case #%d: %s' % (num, status)

n = int(getline())
for x in xrange(n):
    solve(x + 1)

