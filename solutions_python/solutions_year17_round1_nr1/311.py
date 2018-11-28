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
    P = list(map(int, next(infile).split()))
    S = [next(infile).strip() for _ in range(P[0])]
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    import numpy as np

    res = np.asarray([list(s) for s in S])
    def expand(res):
        for i in range(res.shape[0]):
            if sum(l=='?' for l in res[i]) == res.shape[1] and i > 0:
                res[i] = res[i - 1]
            else:
                cc = -1
                for j in range(res.shape[1]):
                    if res[i, j] == '?':
                        if cc < 0:
                            continue
                        else:
                            res[i, j] = res[i, cc]
                    else:
                        cc = j
        return res
    res = expand(res[::-1, ::-1])
    res = expand(res[::-1, ::-1])
    return 'Case #{:d}:\n{}'.format(tc, '\n'.join(''.join(l) for l in res.tolist()))


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
