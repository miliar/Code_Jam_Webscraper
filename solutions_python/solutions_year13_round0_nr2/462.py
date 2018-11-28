#!/usr/bin/env python

from numpy import *

def testField(field):
    if field.max() > 100:
        return False
    maxInRow = field.max(1)
    maxInColumn = field.max(0)
    for i in xrange(field.shape[0]):
        for j in xrange(field.shape[1]):
            if field[i, j] < maxInRow[i] and field[i, j] < maxInColumn[j]:
                return False
    return True

def solve():
    nCases = int(raw_input())
    for nCase in xrange(1, nCases + 1):
        n, m = map(int, raw_input().split())
        field = zeros((n, m))
        for i in xrange(n):
            field[i, :] = array(map(int, raw_input().split()))
        if testField(field):
            print "Case #%d: YES" % nCase
        else:
            print "Case #%d: NO" % nCase

if __name__ == "__main__":
    solve()
