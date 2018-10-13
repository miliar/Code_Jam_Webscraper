#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

def solve():
    N = read_int()
    A = [0] * N
    B = [0] * N
    for i in xrange(N):
        A[i], B[i] = read_ints()
    
    count = 0
    for i in xrange(N):
        for j in xrange(i, N):
            if A[i] > A[j] and B[i] < B[j] or A[i] < A[j] and B[i] > B[j]:
                #print A[i], B[i]
                #print A[j], B[j]
                count = count + 1
    print count
        

def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
