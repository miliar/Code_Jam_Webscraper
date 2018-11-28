#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()

def srl(proc=None):
    if proc is not None:
        return map(proc, rl().split())
    else:
        return rl().split()

SYMS = ".+xo"

def build_ans(orig, now):
    N = len(orig)
    val = 0
    ans = []
    for row in now:
        for v in row:
            val += (v & 1) + (v >> 1)

    for i in xrange(N):
        for j in xrange(N):
            if orig[i][j] != now[i][j]:
                ans.append((SYMS[now[i][j]], i, j))
    return val, ans


def fill1(A):
    N = len(A)
    f0 = [1] * (2 * N)
    f1 = [1] * (2 * N)

    for i in xrange(N):
        for j in xrange(N):
            if A[i][j] & 1:
                f0[i+j] = 0
                f1[i-j+N] = 0

    for i in xrange((N+1)/2):
        for j in xrange(i, N-i):
            for i0, j0 in ((i, j), (j, i), (N-i-1, j), (j, N-i-1)):
                if f0[i0+j0] and f1[i0-j0+N]:
                    A[i0][j0] |= 1
                    f0[i0+j0] = 0
                    f1[i0-j0+N] = 0


def fill2(A):
    N = len(A)
    rf = [1] * N
    cf = [1] * N

    for i in xrange(N):
        for j in xrange(N):
            if A[i][j] & 2:
                rf[i] = 0
                cf[j] = 0

    ri = [i for i, v in enumerate(rf) if v]
    ci = [i for i, v in enumerate(cf) if v]
    for i, j in zip(ri, ci):
        A[i][j] |= 2


def main():
    T = rl(int)
    for t in xrange(1, T+1):
        N, M = srl(int)
        A = [[0] * N for _ in xrange(N)]

        for _ in xrange(M):
            tp, r, c = srl()
            r = int(r) - 1
            c = int(c) - 1
            A[r][c] = SYMS.index(tp)

        orig = [[v for v in vv] for vv in A]

        fill1(A)
        fill2(A)

        val, ans = build_ans(orig, A)
        print "Case #%d: %d %d" % (t, val, len(ans))
        for tp, r, c in ans:
            print tp, r+1, c+1

if __name__ == '__main__':
    main()
