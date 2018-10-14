# -*- coding: utf-8 -*-

T = int(raw_input())
for case in xrange(1, T + 1):
    N = int(raw_input())
    elems = [int(x) for x in raw_input().split(' ')]
    id_and_elems = zip(xrange(1, N + 1), elems)
    perfect_permutation = [x for x in id_and_elems if x[0] != x[1]]
    print 'Case #%d: %.6f' % (case, len(perfect_permutation))

