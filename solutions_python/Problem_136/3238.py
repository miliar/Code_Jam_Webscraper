#!/usr/bin/env python


def f1(C, F, X, n):
    return float(X) / (2 + F * n)


def f2(C, F, X, n):
    t1 = float(C) / (2 + F * n)
    t2 = float(X) / (2 + F * (n + 1))
    return t1 + t2


def f2p(C, F, X, n):
    return float(C) / (2 + F * n)


T = int(raw_input())
for i in xrange(1, T + 1):
    C, F, X = map(float, raw_input().strip().split())

    total_t = 0
    n = 0
    while f1(C, F, X, n) > f2(C, F, X, n):
        t1 = f2p(C, F, X, n)
        n += 1
        total_t += t1
    print 'Case #%d: %.7f' % (i, total_t + f1(C, F, X, n))
