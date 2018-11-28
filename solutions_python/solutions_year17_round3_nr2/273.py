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
    I = [list(map(int, next(infile).split())) for _ in range(P[0] + P[1])]
    #T = next(infile).split()
    #S = [next(infile).strip() for _ in range(P[0] + P[1])]
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    AC, AJ = P
    I = [(b, e, i < AC) for i, (b, e) in enumerate(I)]
    I.sort()
    res = 4
    for cb in range(720):
        ce = cb + 720
        for p in [True, False]:
            if all(p!=bp or (b>=cb and e<=ce) for b, e, bp in I)\
                and all(p==bp or (e<=cb or b>=ce) for b, e, bp in I):
                res = 2

    return 'Case #{:d}: {}'.format(tc, res)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
