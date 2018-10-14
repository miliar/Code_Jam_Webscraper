#!/usr/bin/env python

import sys


def strategy(M, S):
    (sum, ret) = (0, 0)
    for i in range(M):
        sum += S[i]
        if sum < i + 1:
            sum += 1
            ret += 1
    return ret


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline().split()
        M = int(line[0])
        S = [int(x) for x in list(line[1])]
        print 'Case #%s: %s' % (i + 1, strategy(M, S))

main(sys.stdin)
