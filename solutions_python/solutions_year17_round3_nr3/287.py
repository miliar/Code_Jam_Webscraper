# -*- coding: utf-8 -*-
import sys
rl = lambda: sys.stdin.readline().strip()


T = int(rl())
for tcase in range(1, T + 1):
    N, K = map(int, rl().split())
    U = float(rl())
    P = map(float, rl().split())
    print >> sys.stderr, tcase, N, K
    print >> sys.stderr, U
    print >> sys.stderr, P
    while True:
        if U <= 0.0:
            break
        min_p = min(P)
        min_count = P.count(min_p)
        sub_p = filter(lambda x: x > min_p, P)
        if not sub_p:
            P = [min(p + (U / min_count), 1.0) for p in P]
            U = 0.0
        else:
            step = min(sub_p) - min_p
            if step * min_count > U:
                step = U / min_count
            P = [min(p + step, 1.0) if p == min_p else p for p in P]
            U -= (step * min_count)
    s = 1
    for p in P:
        s *= p
    print >> sys.stderr, P, s
    print 'Case #%d: %f' % (tcase, s)
