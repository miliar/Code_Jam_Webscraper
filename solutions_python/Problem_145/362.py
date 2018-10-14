#!/usr/bin/env python

import sys
from fractions import gcd

cases = int(sys.stdin.readline())

for case in range(cases):
    s = sys.stdin.readline()
    p, q = s.split('/')
    p = int(p)
    q = int(q)
    g = gcd(p, q)
    p /= g
    q /= g

    powers = [2**n for n in range(41)]

    if q not in powers:
        print('Case #{}: impossible'.format(case+1))
        continue

    for i in range(1, 40):
        if p * 2 == q:
            print('Case #{}: {}'.format(case+1, i))
            break

        if p * 2 < q:
            p *= 2
            if p%2 == 0 and q%2 == 0:
                p /= 2
                q /= 2
        elif p * 2 > q:
            print('Case #{}: {}'.format(case+1, i))
            break
    else:
        print('Case #{}: impossible'.format(case+1))
