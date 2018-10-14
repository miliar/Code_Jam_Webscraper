#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import functools

def f(pos_o, pos_b, rp):
    c = rp[0][0]
    seq = [int(p) for _, p in itertools.takewhile(lambda (r,_): r==c, rp)]
    d = 0
    last_p = pos_o if c == 'O' else pos_b
    for p in seq:
        d += abs(p - last_p)
        last_p = p
    res = d + len(seq)
    rest = rp[len(seq):]
    if not rest:
        return res
    next_pos = int(rest[0][1])
    if c == 'O':
        pos_o = seq[-1]
        if abs(next_pos - pos_b) <= res:
            pos_b = next_pos
        elif next_pos > pos_b:
            pos_b += res
        else:
            pos_b -= res
    else:
        pos_b = seq[-1]
        if abs(next_pos - pos_o) <= res:
            pos_o = next_pos
        elif next_pos > pos_o:
            pos_o += res
        else:
            pos_o -= res
    return res + f(pos_o, pos_b, rest)
 
t = int(raw_input())
for case in range(1, t+1):
    data = raw_input().split()
    n = int(data[0])
    it = iter(data[1:])
    rp = zip(it, it)
    assert len(rp) == n
    res = f(1, 1, rp)
    print 'Case #{0}: {1}'.format(case, res)

