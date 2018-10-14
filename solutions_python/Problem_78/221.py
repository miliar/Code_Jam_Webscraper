#!/usr/bin/env python2.6

import sys
from fractions import gcd

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

def solve():
    n, pd, pg = read_ints()
    #print n, pd, pg
    g = gcd(pd, 100)
    a = pd / g
    b = 100 / g
    g = gcd(pg, 100)
    c = b * pg / g
    d = b * 100 / g
    #print 'a = %d b = % d c = %d d = %d n = %d' % (a, b, c, d, n)
    #print 'b <= n', b <= n
    #print 'd - b >= c - a', d - b >= c - a
    #print 'c >= a', c >= a
    if b <= n and d - b >= c - a and c >= a:
        if a * 100 / b != pd: print '*********'
        if c * 100 / d != pg: print '+++++++++'
        print 'Possible'
    else:
        print 'Broken'

def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
