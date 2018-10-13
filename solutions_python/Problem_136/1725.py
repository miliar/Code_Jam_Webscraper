#!/usr/bin/python

import sys

with open(sys.argv[1], 'r') as f:
    T = int(f.readline().strip())

    for _t in xrange(1, T+1):
        C, F, X = map(float, f.readline().strip().split())
        # print C, F, X

        best = X/2
        n = 1
        while True:
            # print best
            _best = sum([C/(2+k*F) for k in xrange(n)]) + X/(2+n*F)
            if _best < best:
                best = _best
                n += 1
            else:
                break

        print 'Case #%d: ' % _t + '%.7f' % best
        # raw_input()