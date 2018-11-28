# -*- encoding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division


def fix(n):
    if n < 10:
        return n
    s = str(n)
    ndigs = len(s)
    for idx, (prev, curr) in enumerate(zip(s, s[1:])):
        if int(prev) > int(curr):
            power = 10 ** (ndigs - idx - 1)
            return (n - power) - (n % power) + (power - 1)
    return n


n_cases = int(input())
for ctr in range(n_cases):
    n = int(input())

    while fix(n) != n:
        n = fix(n)

    print('Case #%d: %d' % (ctr+1, n))
