# -*- coding: utf-8 -*-

from fractions import Fraction as F

T = int(raw_input())
for case in xrange(1, T + 1):
    div = map(int, raw_input().split(' '))
    L, t, N, C = div[:4]
    A = div[4:]

    stars = A * (N / C + 1)
    stars = stars[:N]

    tm = 0
    for i in xrange(N):
        tm += stars[i] * 2
        if t <= tm:
            break
    n_before = i

    before = stars[:n_before]
    if sum(before) * 2 != t:
        left = stars[n_before] - F(1, 2) * (t - sum(before) * 2)
        after = stars[n_before+1:]
    else:
        left = 0
        after = stars[n_before:]

    cand = [left] + after
    cand.sort(reverse=True)

    hours = sum(stars) * 2
    for i in xrange(L):
        try:
            hours -= cand[i]
        except IndexError:
            pass

    print 'Case #%d: %d' % (case, hours)


