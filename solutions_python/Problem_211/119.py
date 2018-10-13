#!/usr/bin/env python

from operator import mul


def row(fn):
    return map(fn, raw_input().strip().split())


for t in xrange(1, input()+1):
    N, K = row(int)
    assert N == K
    U = input()
    P = row(float)

    mi = min(P)
    count = P.count(mi)
    P = [p for p in P if p != mi]

    while U and mi < 1.0:
        next = min(P) if P else 1.0
        if U < count * (next - mi):
            mi += (U / count)
            break
        else:
            U -= count * (next - mi)
            count += P.count(next)
            P = [p for p in P if p != next]
            mi = next

    res = (mi**count)
    if P: res *= reduce(mul, P)
    print 'Case #%d: %f' % (t, res)
