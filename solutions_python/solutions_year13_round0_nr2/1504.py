#!/usr/bin/env python
import sys

def check(B, N, M):
    rowmax = range(N)
    colmax = range(M)

    for r in range(N):
        rowmax[r] = 0
        for c in range(M):
            rowmax[r] = max(rowmax[r], B[r][c])

    for c in range(M):
        colmax[c] = 0
        for r in range(N):
            colmax[c] = max(colmax[c], B[r][c])

    for r in range(N):
        for c in range(M):
            if B[r][c] < rowmax[r] and B[r][c] < colmax[c]:
                return False

    return True

def solve():
    N, M = sys.stdin.readline().split()
    N = int(N)
    M = int(M)
    B = []
    for i in range(N):
        B.append(sys.stdin.readline().split())

    if check(B, N, M):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        print 'Case #%d: %s' % (t, solve())
