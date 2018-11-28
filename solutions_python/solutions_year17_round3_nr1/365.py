"""Usage:
    pypy3 -u X.py < X-test.in > X-test.out
or sometimes:
    python3 -u X.py < X-test.in > X-test.out
"""
from __future__ import print_function

import sys


def common_setup():
    pass


def case_reader(tc, infile):
    #N = int(next(infile))
    P = list(map(int, next(infile).split()))
    I = [list(map(int, next(infile).split())) for _ in range(P[0])]
    #T = next(infile).split()
    #S = [next(infile).strip() for _ in range(N)]
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    import math
    N, K = P
    res = 0.
    for i, (r, h) in enumerate(I):
        rres = r ** 2 + r * 2 * h
        II = [(rr, hh) for ii, (rr, hh) in enumerate(I) if rr <= r and ii != i]
        if len(II) < K - 1:
            continue
        for rr, hh in sorted(II, key=lambda x: x[0] * x[1], reverse=True)[:K - 1]:
            rres += rr * 2 * hh
        res = max(res, rres)
    return 'Case #{:d}: {}'.format(tc, res * math.pi)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
