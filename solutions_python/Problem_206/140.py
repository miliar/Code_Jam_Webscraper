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
    P = list(map(int, next(infile).split()))
    I = [list(map(int, next(infile).split()) )for _ in range(P[1])]
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    D, N = P
    t = 0
    for k, s in I:
        t = max(t, (D - k) / s)
    return 'Case #{:d}: {}'.format(tc, D / t)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
