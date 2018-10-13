#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import math

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in raw_input().split()]
def readint(): return int(raw_input().strip())

debug = lambda x: None

def calc(A, B):
    """
    n = n_0 n_1...n_l-1
    -> m = n_k...n_l-1 n_0 n_1...n_k-1 (k = 1...l-1)

    O(B * log(B))
    """
    iA = int(A)
    iB = int(B)

    assert 1 <= iA <= iB

    result = 0

    for n in range(iA, iB):
        strn = str(n)
        ms = set()

        for k in range(1, len(strn)):
            strm = strn[k:] + strn[:k]
            m = int(strm)
            if n < m <= iB:
                debug('{0} < {1}'.format(n, m))
                ms.add(m)

        result += len(ms)

    return result

T = readint()
for i in xrange(T):
    A, B = raw_input().split()
    print('Case #{0}: {1}'.format(i + 1, calc(A, B)))
