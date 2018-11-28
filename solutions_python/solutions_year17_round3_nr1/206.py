"""
Google Code Jam
2017 Round 1C

Problem A. 
    :author: yamaton
    :date: 2016-04-30
"""
from __future__ import absolute_import, division, print_function

# import itertools as it
# import collections
import sys
import math


def solve(pairs, n, k):
    sides = sorted([(2 * r * h, r * (r + 2 * h), r) for (r, h) in pairs], reverse=True)
    candidates = [pair[0] for pair in sides[:k]]
    rs = [pair[2] for pair in sides[:k]]
    rmax = max(pair[2] for pair in sides)
    rest = [pair[1] for pair in sides[k:]]

    pp('sides', sides)

    total = sum(candidates)
    if rmax in rs:
        pp('no prob')
        return math.pi * (total + rmax * rmax)
    else:
        pp('mixed')
        tmp = max(total - out_ + in_
                  for out_ in candidates
                  for in_ in rest)
        rloc = max(rs)
        return math.pi * max(tmp, total + rloc * rloc)


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input()) + 1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d: " % _tc, end='')
        n, k = map(int, input().split())
        pairs = [tuple(map(int, input().split())) for _ in range(n)]

        result = solve(pairs, n, k)
        pp()
        pp('(n, k) =', (n, k))
        pp('pairs =', pairs)
        pp('result = %0.9f' % result)
        print("%0.9f" % result)


if __name__ == '__main__':
    main()
