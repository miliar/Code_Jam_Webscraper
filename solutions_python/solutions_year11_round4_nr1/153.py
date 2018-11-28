#!/opt/local/bin/python

import sys
from itertools import count
from fractions import Fraction

input_it = iter(sys.stdin.readlines())

T = int(input_it.next())

for case in range(T):
    (X, S, R, u, N) = tuple(int(i) for i in input_it.next().split())

    B = []
    E = []
    w = []
    for n in range(N):
        (b, e, v) = tuple(int(i) for i in input_it.next().split())
        B.append(b)
        E.append(e)
        w.append(v)

    l = [float(0) for i in range(101)]
    l[0] = float(X)
    for (b, e, v) in zip(B, E, w):
        l[v] += e - b
        l[0] -= e - b

    result = float(0)
    t_left = float(u)
    for v, l_i in enumerate(l):
        if t_left < 0:
            result += l_i / (S + v)
        elif t_left * (R + v) >= l_i:
            result += l_i / (R + v)
            t_left -= l_i / (R + v)
        else:
            d_left = t_left * (R + v)
            result += t_left + (l_i - d_left) / (S + v)
            t_left = float(0)

    print 'Case #%s: %.9f' % (case + 1, result)

