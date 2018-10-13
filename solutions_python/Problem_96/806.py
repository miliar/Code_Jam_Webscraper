#!/usr/bin/env python
import sys
import itertools


def log(fmt, *args):
    sys.stderr.write((fmt + '\n') % args)

def read_int():
    return int(raw_input())

def read_ints():
    return [int(s) for s in raw_input().split()]


def do_case():
    ints = read_ints()
    N, S, p = ints[:3]
    t = ints[3:]
    assert len(t) == N

    lut = [(0, 1, 1), (1, 1, 2)]

    max_count = 0
    q = [ti // 3 for ti in t]
    r = [ti % 3 for ti in t]

    for s_indices in itertools.combinations(xrange(N), S):
        surprising = [0] * N
        for si in s_indices:
            surprising[si] = 1

        count = 0
        for i in xrange(N):
            if t[i] in (0, 1):
                best = t[i]
            elif t[i] == 2:
                best = 2 if surprising[i] else 1
            else:
                best = q[i] + lut[surprising[i]][r[i]]

            if best >= p:
                count += 1
            #log('t=%s q=%s r=%s surprising=%s best=%s [%s]',
            #    t[i], q[i], r[i], surprising[i], best, best >= p)

        max_count = max(max_count, count)
    
    return max_count


for case in xrange(read_int()):
    print 'Case #%d: %s' % (case + 1, do_case())
