# Problem C. Bathroom Stalls

import os

SOURCE = '%s/../Resources/Q1Cl.in' % os.path.dirname(__file__)
TARGET = '%s/../Resources/Q1Cl.out' % os.path.dirname(__file__)

INPUT = open(SOURCE).read().splitlines()
OUTPUT = open(TARGET, 'w')

T = int(INPUT.pop(0))
for t0 in xrange(T):
    print >> OUTPUT, 'Case #%d:' % (t0 + 1),

    N, K = map(int, INPUT.pop(0).split())

    Q = K - 1
    seg = {N: 1}
    while Q > 0:
        if not seg:
            break

        s = max(seg)
        v = seg[s]
        if v > Q:
            break
        else:
            del seg[s]
            Q -= v

        a, r = s >> 1, s & 1  # divmod(s, 2)
        if a > 1:
            seg[a] = seg.setdefault(a, 0) + v
            if r == 1:
                seg[a] = seg[a] + v
            elif a > 2:
                seg[a - 1] = seg.setdefault(a - 1, 0) + v

    if seg:
        m = max(seg)
        a, r = m >> 1, m & 1

        res = (a, a if r == 1 else a - 1)
    else:
        res = (0, 0)

    print >> OUTPUT, '%s %s' % res
