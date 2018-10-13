# Problem A.

import os
import math
import itertools

SMALL = True
SOURCE = '%s/../Resources/R1A%s.in' % (os.path.dirname(__file__), 's' if SMALL else 'l')
TARGET = '%s/../Resources/R1A%s.out' % (os.path.dirname(__file__), 's' if SMALL else 'l')

INPUT = open(SOURCE).read().splitlines()
OUTPUT = open(TARGET, 'w')

PI = math.pi

T = int(INPUT.pop(0))
for t0 in xrange(T):
    print >> OUTPUT, 'Case #%d:' % (t0 + 1),
    print 'Case #%d:' % (t0 + 1)

    P = []

    N, K = map(int, INPUT.pop(0).split())
    for n0 in xrange(N):
        Ri, Hi = map(float, INPUT.pop(0).split())
        P.append((Ri, Hi, PI * Ri**2, 2 * PI * Ri * Hi))
        # P.append((Ri, Hi))

    SOL = 0.0

    for c in itertools.combinations(sorted(P, cmp=lambda x, y: cmp(x[0], y[0]) or cmp(y[1], x[1])), K):
        s = 0.0
        r0 = 0.0
        for _, _, r, h in c:
            s += r - r0 + h
            r0 = r

        # if s > SOL:
        #     print 'max :', c, s
        # else:
        #     print 'less:', c, s

        SOL = max(SOL, s)

    # print N, K, P

    print >> OUTPUT, '%.6f' % SOL
    print '%.6f' % SOL
