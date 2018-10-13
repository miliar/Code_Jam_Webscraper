#!/usr/bin/env python2.7

IMPOSSIBLE = 'IMPOSSIBLE'
EPS = 1.0e-7

T = int(raw_input())
for x in xrange(1, T + 1):
    N, V, X = map(float, raw_input().split())
    N = int(N)
    R, C = zip(*[map(float, raw_input().split()) for j in xrange(N)])
    res = IMPOSSIBLE
    if min(C) - EPS < X < max(C) + EPS:
        if N == 1:
            res = V / R[0]
        else:
            if abs(C[0] - C[1]) < EPS:
                res = V / (R[0] + R[1])
            else:
                if abs(C[0] - X) < EPS:
                    res = V / R[0]
                elif abs(C[1] - X) < EPS:
                    res = V / R[1]
                else:
                    r = (X - C[0]) / (C[1] - X)
                    v0 = V * 1.0 / (1.0 + r)
                    v1 = V * r / (1.0 + r)
                    res = max(v0 / R[0], v1 / R[1])
    print 'Case #{}: {}'.format(x, res)
