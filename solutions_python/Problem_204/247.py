"""
Google Code Jam
2017 Round 1A

Problem B
    :author: yamaton
    :date: 2017-04-14
"""

import sys
import math
import itertools as it


def segment(r, amount):
    p = amount / r
    lb = math.ceil(p / 1.1)
    ub = math.floor(p / 0.9)
    return set(range(lb, ub + 1)) - {0}


def count(rs, kit):
    segments = [segment(r, k) for (r, k) in zip(rs, kit)]
    res = set.intersection(*segments)
    # pp('kit =', kit)
    # pp('res =', res)
    if res:
        return 1
    else:
        return 0


def solve(rs, qss):
    n = len(qss)
    p = len(qss[0])
    assert n <= 2
    assert p <= 8

    if n == 1:
        return sum(count(rs, [k]) for k in qss[0])
    else:
        res = 0
        for indices in it.permutations(range(p)):
            xs0 = [qss[0][i] for i in indices]
            xs1 = qss[1]
            xss = [list(line) for line in zip(*[xs0, xs1])]
            out = sum(count(rs, xs) for xs in xss)
            if out == p:
                return out
            res = max(res, out)
        return res


def pp(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    for _tc in range(1, int(input()) + 1):
        pp('\n--------- case #%d -------' % _tc)
        print("Case #%d: " % _tc, end='')
        n, p = map(int, input().split())
        rs = [int(c) for c in input().split()]
        assert len(rs) == n
        qss = [[int(c) for c in input().split()] for _ in range(n)]
        assert len(qss[0]) == p

        result = solve(rs, qss)
        pp()
        pp('rs =', rs)
        pp('qss =', qss)
        pp('result =', result)
        print(result)


if __name__ == '__main__':
    main()
