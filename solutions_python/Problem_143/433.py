#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for i in range(T):
        A, B, K = list(map(int, sys.stdin.readline().split()))
        
        sol = []
        for a in range(A):
            for b in range(B):
                if a & b < K:
                    sol.append((a, b, a & b))
        
        print('Case #%d: %d' % (i + 1, len(sol)))
