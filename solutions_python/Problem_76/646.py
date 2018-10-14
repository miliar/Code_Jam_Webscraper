#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

# this is a stupid algorithm, will only work for small N
def solve():
    N = read_int()
    C = read_ints()
    max = 0
    for i in range(1, 2**N - 1):
        s = p = f = 0
        for bit in range(0, N):
            if i & (1 << bit):
                s += C[bit]
                f ^= C[bit]
            else:
                p ^= C[bit]
        if f == p and s > max:
            max = s;
    print max if max != 0 else "NO"

def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
