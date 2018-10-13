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
    N = int(next(infile))
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):

    res = str(N)
    n = 2
    while True:
        if n > len(res):
            break
        if int(res[-n]) <= int(res[1-n]):
            n += 1
        else:
            res = str(int(str(int(res[:-n+1]) - 1) + '9' * (n - 1)))
            n += 1
    return 'Case #{:d}: {}'.format(tc, res)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
