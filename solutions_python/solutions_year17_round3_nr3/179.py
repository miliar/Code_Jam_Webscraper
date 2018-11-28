"""
Google Code Jam
2017 Round 1C

Problem C. 
    :author: yamaton
    :date: 2016-04-30
"""
from __future__ import absolute_import, division, print_function

import operator
import functools
# import collections
import sys


def solve(n, k, u, ps):
    ps = sorted(ps)
    if k == 1:
        return min(1.0, ps[-1] + u)

    for i in range(k - 1):
        inc = ps[i + 1] - ps[i]
        # pp('inc =', inc)
        if inc * (i + 1) <= u:
            u -= inc * (i + 1)
        else:
            val = ps[i] + u / (i + 1)
            pp('leaving at', i, 'with val =', val)
            return val ** (i + 1) * functools.reduce(operator.mul, ps[i + 1:], 1.0)

    return min((ps[-1] + u / n) ** k, 1.0)


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input()) + 1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d: " % _tc, end='')
        n, k = map(int, input().split())
        u = float(input())
        ps = [float(s) for s in input().split()]
        assert len(ps) == n
        result = solve(n, k, u, ps)
        pp()
        pp('(n, k) =', (n, k))
        pp('u =', u)
        pp('ps =', ps)
        pp('result =', result)
        print(result)


if __name__ == '__main__':
    main()
