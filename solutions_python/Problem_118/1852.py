#!/usr/bin/env python2
# c
import itertools
import math

with open('c.in') as f:
    t = int(f.readline())

    for tt in xrange(t):
        lower, upper = map(int, f.readline().strip().split())
        result = 0

        for v in itertools.count(int(math.sqrt(lower))):
            v_2 = v ** 2

            if v_2 > upper:
                break

            if v_2 < lower:
                continue

            v_str = str(v)
            v_2_str = str(v_2)

            if v_str == v_str[::-1] and v_2_str == v_2_str[::-1]:
                result += 1

        print "Case #{0}: {1}".format(tt + 1, result)
