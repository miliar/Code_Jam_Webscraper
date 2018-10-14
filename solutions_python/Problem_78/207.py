#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def gcf(a, b):
    m = 1
    for _i in xrange(1, a + 1):
        if a % _i == 0 and b % _i == 0:
            m = _i
    return m

def doit(n, pd, pg):
    if pg == 100 and pd == 100:
        return True
    elif pg == 0 and pd == 0:
        return True
    if pg == 100 and pd != 100:
        return False
    elif pg == 0 and pd != 0:
        return False
    elif 100 / gcf(pd, 100) > n:
        return False
    return True

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        if sys.argv[1] != '-':
            fn = sys.argv[1]
            f = open(fn)
    t = int(f.readline())
    for _t in xrange(t):
        n, pd, pg = map(int, f.readline().split())
        if doit(n, pd, pg) == False:
            print 'Case #{0}: Broken'.format(_t + 1)
        else:
            print 'Case #{0}: Possible'.format(_t + 1)
