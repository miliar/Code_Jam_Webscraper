#!/usr/bin/env python

def row(fn):
    return map(fn, raw_input().strip().split())

def normalize(T):
    T = [(s, e if e > s else e + 24*60) for s, e in T]
    return sorted(T)

for t in xrange(1, input()+1):
    Ac, Aj = row(int)
    Tc = normalize([row(int) for _ in xrange(Ac)])
    Tj = normalize([row(int) for _ in xrange(Aj)])

    assert 1 <= Ac + Aj <= 2

    if Ac == 2:
        time = min(
            Tc[1][1] - Tc[0][0],
            (24*60 - Tc[1][0]) + Tc[0][1]
        )
        res = 2 if time <= 720 else 4
    elif Aj == 2:
        time = min(
            Tj[1][1] - Tj[0][0],
            (24*60 - Tj[1][0]) + Tj[0][1]
        )
        res = 2 if time <= 720 else 4
    else:
        res = 2

    print 'Case #%d: %d' % (t, res)
