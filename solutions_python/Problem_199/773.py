# Problem A. Oversized Pancake Flipper

import os

SOURCE = '%s/../Resources/Q1Al.in' % os.path.dirname(__file__)
TARGET = '%s/../Resources/Q1Al.out' % os.path.dirname(__file__)

INPUT = open(SOURCE).read().splitlines()
OUTPUT = open(TARGET, 'w')

T = int(INPUT.pop(0))
for t0 in xrange(T):
    print >> OUTPUT, 'Case #%d:' % (t0 + 1),

    S, K = INPUT.pop(0).split()
    A, K = ['+' == s for s in S], int(K)
    L = len(A)

    r = 0

    for i, a in enumerate(A):
        if not a:
            if i + K > L:
                print >> OUTPUT, 'IMPOSSIBLE'
                break

            r += 1
            for k in xrange(K):
                A[i+k] = not A[i+k]

    else:
        print >> OUTPUT, r
