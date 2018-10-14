#!/usr/bin/python

N = int(raw_input())
for case in range(1, N + 1):
    T = int(raw_input())
    NA, NB = map(lambda x: int(x), raw_input().split(' '))
    A = [tuple(map(lambda x: int(x[0:2]) * 60 + int(x[3:5]), raw_input().split(' '))) for x in range(NA)]
    B = [tuple(map(lambda x: int(x[0:2]) * 60 + int(x[3:5]), raw_input().split(' '))) for x in range(NB)]
    a = b = c = 0
    na = nb = 0
    for time in xrange(1440):
        n = len(filter(lambda x: x[1] + T == time, A))
        b += n
        c -= n
        n = len(filter(lambda x: x[1] + T == time, B))
        a += n
        c -= n
        n = len(filter(lambda x: x[0] == time, A))
        a -= n
        c += n
        n = len(filter(lambda x: x[0] == time, B))
        b -= n
        c += n
        if a < 0:
            na -= a
            a = 0
        if b < 0:
            nb -= b
            b = 0
    print 'Case #%d:' % case, na, nb
