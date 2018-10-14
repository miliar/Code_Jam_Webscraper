# -*- coding: utf-8 -*-

from fractions import Fraction as F

def toF(xs):
    ret = []
    for x in xs:
        ret.append(F(x))
    return ret

T = int(raw_input())
for case in xrange(1, T + 1):
    X, S, R, t, N = toF(map(int, raw_input().split(' ')))
    W = []  # (B, E, w)
    for i in xrange(int(N)):
        W.append(toF(map(int, raw_input().split(' '))))

    W.sort(key=lambda x: x[2])
    corridor_length = 0
    for b, e, w in W:
        corridor_length += e - b
    normal_length = X - corridor_length
    W.insert(0, toF([0, normal_length, 0]))

    total_time = F(0)
    for b, e, w in W:
        if 0 < t:
            run = (R + w) * t
            if run <= e - b:
                total_time += t
                t = 0
                total_time += (e - b - run) / (S + w)
            else:
                run_time = (e - b) / (R + w)
                t -= run_time
                total_time += run_time
        else:
            total_time += (e - b) / (S + w)

    print 'Case #%d: %.7f' % (case, total_time)

