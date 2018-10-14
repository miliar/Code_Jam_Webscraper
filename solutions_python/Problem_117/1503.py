#!/usr/bin/env python

import sys


def validBlock(N, R, i, j, RowMax, ColMax):
    if R[i][j] >= RowMax[i]:
        return True
    if R[i][j] >= ColMax[j]:
        return True
    return False


def solve(N, M, R, RowMax, ColMax):
    for i in range(N):
        for j in range(M):
            if not validBlock(N, R, i, j, RowMax, ColMax):
                return "NO"
    return "YES"


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline().split()
        (N, M) = map(int, line)
        R = []
        RowMax = []
        ColMax = []
        for j in range(N):
            line = infile.readline().split()
            R.append(line)
            RowMax.append(max(line))
        for j in range(M):
            ColMax.append(max([R[c][j] for c in range(N)]))
        print 'Case #%s: %s' % (i + 1, solve(N, M, R, RowMax, ColMax))

main(sys.stdin)
