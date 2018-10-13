"""Usage:
    pypy -u X.py < X-test.in > X-test.out
or sometimes:
    python -u X.py < X-test.in > X-test.out
may be python 2 or 3.
"""
from __future__ import print_function

import sys


def common_setup():
    pass


def case_reader(tc, infile):
    P = map(int, next(infile).split())
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    N, K = P
    S = {N: 1}
    while True:
        n = max(S)
        k = S.pop(n)
        if K <= k:
            break
        m = (n - 1) // 2
        S[m] = S.get(m, 0) + k
        S[n - m - 1] = S.get(n - m - 1, 0) + k
        K -= k
    m = (n - 1) // 2
    return 'Case #{:d}: {} {}'.format(tc, n - m - 1, m)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
