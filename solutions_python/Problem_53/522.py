#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import psyco
psyco.full()

def compute(n, k):
    n = 2 ** n
    q, r = divmod(k + 1, n)
    if q > 0 and r == 0:
        return "ON"
    else:
        return "OFF"

if __name__ == '__main__':
    T = input()
    for i in xrange(T):
        N, K = [int(x) for x in raw_input().split()]
        print 'Case #%d: %s' % (i + 1, compute(N, K))
