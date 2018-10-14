#!/usr/bin/env python
#-*- coding: utf-8 -*-

def solve (n):
    ret = 0
    for i in range (1, 1 + int (n ** 0.5)):
        if (str (i) == str (i)[::-1] and str (i * i) == str (i * i)[::-1]):
            ret += 1
    return ret

L = []
ret = 0;
for i in range (0, 10**7 + 1):
    if (str (i) == str (i)[::-1] and str (i * i) == str (i * i)[::-1]):
        ret += 1
    L.append (ret)


T = int (raw_input ())
for t in range (1, T + 1):
    A, B = [int (i) for i in raw_input ().split ()]
    lo = int ((A - 1) ** 0.5)
    hi = int (B ** 0.5)
    print 'Case #{0}: {1}'.format (str (t), str (L [hi] - L [lo]))
