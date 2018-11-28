# Problem A.

import os

SMALL = False
SOURCE = '%s/../Resources/R1A%s.in' % (os.path.dirname(__file__), 's' if SMALL else 'l')
TARGET = '%s/../Resources/R1A%s.out' % (os.path.dirname(__file__), 's' if SMALL else 'l')

INPUT = open(SOURCE).read().splitlines()
OUTPUT = open(TARGET, 'w')

T = int(INPUT.pop(0))
for t0 in xrange(T):
    print >> OUTPUT, 'Case #%d:' % (t0 + 1),

    H = []

    D, N = map(int, INPUT.pop(0).split())
    for n0 in xrange(N):
        Ki, Si = map(float, INPUT.pop(0).split())
        H.append((Ki, Si))

    SOL = D / max((D - k) / s for k, s in H)

    print >> OUTPUT, '%.6f' % SOL
    print '%.6f' % SOL
