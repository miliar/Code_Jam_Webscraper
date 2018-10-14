# Problem B.

import os

SMALL = True
SOURCE = '%s/../Resources/R1B%s.in' % (os.path.dirname(__file__), 's' if SMALL else 'l')
TARGET = '%s/../Resources/R1B%s.out' % (os.path.dirname(__file__), 's' if SMALL else 'l')

INPUT = open(SOURCE).read().splitlines()
OUTPUT = open(TARGET, 'w')

T = int(INPUT.pop(0))
for t0 in xrange(T):
    print >> OUTPUT, 'Case #%d:' % (t0 + 1),

    N, R, O, Y, G, B, V = map(int, INPUT.pop(0).split())

    H = {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}
    # H = {x: y for x, y in H.items() if y > 0}
    print H

    """
    R + Y = O   -- A mane with red and yellow hairs appears orange.
    Y + B = G   -- A mane with yellow and blue hairs appears green.
    R + B = V   -- A mane with red and blue hairs appears violet.
    """

    F = {
        'R': ['G', 'Y', 'B'],
        'Y': ['V', 'R', 'B'],
        'B': ['O', 'R', 'Y'],
        'O': ['B'],
        'G': ['R'],
        'V': ['Y'],
    }

    for k in ('R', 'Y', 'B', 'O', 'G', 'V'):
        if H[k] > 0:
            p = k
            break
    H[p] -= 1

    SOL = [p]
    # L = 1
    while not all(H[k] == 0 for k in H):
        # for f in sorted(F[p], cmp=lambda x, y: 1 if y in ('O', 'G', 'V') else -1 if x in ('O', 'G', 'V') else cmp(H[y], H[x])):
        for f in sorted(F[p], cmp=lambda x, y: cmp(H[y], H[x])):
            if H[f] > 0:
                SOL.append(f)
                # L += 1
                H[f] -= 1
                p = f
                break

        else:
            print 'break on', ''.join(SOL), H
            SOL = None
            break

    if SOL is None:
        print >> OUTPUT, 'IMPOSSIBLE'
        print 'IMPOSSIBLE'

    elif SOL[0] not in F[SOL[-1]]:
        print >> OUTPUT, 'IMPOSSIBLE'
        print 'IMPOSSIBLE - %s' % ''.join(SOL)

    else:
        print >> OUTPUT, ''.join(SOL)
        print ''.join(SOL)

    print
