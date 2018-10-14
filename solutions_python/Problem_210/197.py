"""
Google Code Jam
2017 Round 1C

Problem B.
    :author: yamaton
    :date: 2016-04-30
"""
from __future__ import absolute_import, division, print_function

# import itertools as it
# import collections
import sys


def solve(cs, js):
    if len(cs) + len(js) == 1:
        return 2

    if len(cs) == 1 and len(js) == 1:
        return 2

    if len(cs + js) == 2:
        pairs = sorted(cs + js)
        if pairs[1][1] - pairs[0][0] <= 720:
            return 2
        if pairs[1][0] - pairs[0][1] >= 720:
            return 2
        else:
            return 4


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input()) + 1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d: " % _tc, end='')
        ac, aj = map(int, input().split())
        c_pair = [[int(i) for i in input().split()] for _ in range(ac)]
        j_pair = [[int(i) for i in input().split()] for _ in range(aj)]

        result = solve(c_pair, j_pair)
        pp()
        pp('cd =', c_pair)
        pp('jk =', j_pair)
        pp('result =', result)
        print(result)


if __name__ == '__main__':
    main()
