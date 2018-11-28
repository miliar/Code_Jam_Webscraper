#!/usr/bin/python

import sys, operator

def getint():
    line = sys.stdin.readline().strip()
    return int(line)
def getints():
    return [int(w) for w in sys.stdin.readline().split()]

cases = getint()
for case in range(1, cases + 1):
    N = getint()
    C = getints()
    if reduce(operator.xor, C) == 0:
        C.sort()
        print 'Case #%d:' % case, sum(C) - C[0]
    else:
        print 'Case #%d: NO' % case

# vim:set ts=4 sw=4 et:
