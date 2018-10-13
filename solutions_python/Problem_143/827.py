#-*- coding: utf-8 -*-

import sys

_in = lambda: sys.stdin.readline().strip()

results = [1000000000,1000000000]

def solve():
    A,B,K = [int(x) for x in _in().split()]
    result = 0
    for Ai in xrange(0, A):
        for Bi in xrange(0, B):
            if Ai & Bi < K:
                result += 1

    return result

for T in xrange(0, int(_in()) ):
    print "Case #%d: %s" % (T+1, str(solve()))

