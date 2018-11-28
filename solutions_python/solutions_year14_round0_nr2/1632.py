#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

def next_turn(f):
    C, F, X = map(float, f.readline().replace('\n', '').split(' '))

    mx = X/2

    if C > X:
        return mx

    # naive
    p = mx
    for k in xrange(int(X/C)+1):
        p = min(p, X/(k*F+2) + sum([C/(n*F+2) for n in xrange(k)]))

    return p


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: %s <input file>" % sys.argv[0]
        sys.exit(1)

    with open(sys.argv[1]) as f:
        with open("%s.out" % sys.argv[1], 'w') as out:
            c = int(f.readline())
            for i in range(1, c+1):
                out.write('Case #%d: %.7f\n' % (i, next_turn(f)))
    print 'done.'
