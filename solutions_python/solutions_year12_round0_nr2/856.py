#!/usr/bin/env python

import sys

i = 1

for t in [l.strip() for l in sys.stdin.readlines()][1:]:
    nums = [int(w) for w in t.split()]
    n = nums[0]
    s = nums[1]
    p = nums[2]

    c1 = 0
    c2 = 0

    for n in nums[3:]:
        q = n / 3

        if n % 3:
            q += 1

        if q >= p:
            c1 += 1

        if q == p - 1 and (n % 3 == 2 or n % 3 == 0) and n > 1:
            c2 += 1

    print 'Case #{0}: {1}'.format(i, c1 + min(c2, s))
    i += 1
