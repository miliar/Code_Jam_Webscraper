"""Usage:
    pypy -u X.py < X-test.in > X-test.out
or sometimes
    python -u X.py < X-test.in > X-test.out
"""

import os
import sys


def common_setup():
    pass


def case_reader(tc, infile):
    N = int(next(infile))
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    import itertools as it

    seen = set()
    res = 'INSOMNIA'
    try:
        for i in it.count(1):
            r = i * N
            seen.update(str(r))
            if len(seen) == 10:
                res = r
                break
    except KeyboardInterrupt:
        pass

    return 'Case #{:d}: {}'.format(tc, res)


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print case_solver(**case)
