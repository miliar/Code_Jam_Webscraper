#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()


def check(l, n): 
    if n == 1:
        return True
    else:
        return n in l and check(l, 1 + l.index(n))

def count(n):
    p = set(xrange(2, n + 1)) 
    r = 0 
    for i in xrange(len(p) + 1): 
        from itertools import combinations
        for l in combinations(p, i): 
            if check(l, n): 
                r += 1
    return r

def solve(r):
    n = read_int()
    print r[n - 2]

def main():
    T = read_int()
    r = [count(x) % 100003 for x in range(2, 26)]
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve(r)

if __name__ == '__main__':
    main()
