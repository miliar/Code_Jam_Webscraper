#!/usr/bin/env python

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def solve():
    N, K = read_ints()

    b = ''
    while K > 0:
        if K % 2 == 0:
            b = '0' + b
        else:
            b = '1' + b
        K = K / 2
    
    if b.endswith('1' * N):
        print 'ON'
    else:
        print 'OFF'

def main():
    T = read_int()

    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
