#!/usr/bin/env python
# encoding: utf-8

import math
from copy import copy

from contextlib import nested

debug = False
verbose = False


def solve(x, l):
    if debug and verbose:
        print x, l
    max_v = max(x)
    max_v_cnt = x.count(max_v)
    t = max_v + len(x) - l
    t_x = x
    max_k = int(math.ceil(math.sqrt(max_v))) + 1
    for k in reversed(xrange(2, max_k)):
        new_vals = [max_v / k] * k * max_v_cnt
        if max_v % k > 0:
            for i in range(max_v_cnt):
                new_vals[i] += max_v % k
        y = copy(x)
        for i in range(max_v_cnt):
            y.remove(max_v)
        y.extend(new_vals)
        new_t = max(y) + len(y) - l
        if new_t < t:
            t = new_t
            t_x = y
        tt, tt_x = solve(y, l)
        if tt < t:
            t = tt
            t_x = tt_x
        if debug and verbose:
            print 'x:', sorted(x), 'k:', k, ' new_vals:', new_vals, \
                  ' y:', sorted(y), ' t:', t
    return t, t_x

if __name__ == '__main__':
    finame = 'B-small-attempt2.in'
    foname = 'B-small-attempt2.out'
    if debug:
        finame = 'B-small1.in'
        foname = 'B-small1.out'
    with nested(open(finame),
                open(foname, 'w')) as (fi, fo):
        num_case = int(fi.readline().strip())
        for i in range(1, num_case + 1):
            if debug:
                print '=== Case: %d ===' % i
            d = int(fi.readline().strip())
            x = map(int, fi.readline().strip().split(' '))
            ret = solve(x, len(x))
            if debug:
                print 'Case #%d: %d - %s - %s' % \
                    (i, ret[0],
                     ', '.join(map(str, x)),
                     ', '.join(map(str, ret[1])))
            fo.write('Case #%d: %d\n' % (i, ret[0]))
