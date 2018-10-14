#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

def solve():
    A, B = read_ints()
    count = 0
    for n in range(A, B):
        old_n = n
        n = str(n)
        for m in range(old_n + 1, B + 1):
            m = str(m)
            r = False
            for i in range(1, len(n)):
                if n[i:] + n[0:i] == m:
                    r = True
                    break
            if r:
                count += 1
    print count

def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
