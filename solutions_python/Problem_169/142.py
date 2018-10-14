#!/usr/bin/python

import sys, decimal as dec, collections as coll, itertools as itt, fractions as frac, math

if len(sys.argv) >= 2 and sys.argv[1] == 'debug':
    DEBUG = True
else:
    DEBUG = False




_T = int(raw_input())
_tt = max(_T/10, 1)

for _cc in xrange(_T):
    print 'Case #{}:'.format(_cc+1),
    if _cc % _tt == 0:
        print >>sys.stderr, 'Solving: ', (_cc+1)*100/_T, '%'

    # N = int(raw_input())
    ss = raw_input().split()

    N, V, X = int(ss[0]), frac.Fraction(ss[1]), frac.Fraction(ss[2])

    sumrcl, sumrch = frac.Fraction(0), frac.Fraction(0)
    sumrl, sumrh = frac.Fraction(0), frac.Fraction(0)

    exactR = 0

    for i in xrange(N):
        R, C = map( frac.Fraction, raw_input().split() )
        if C == X:
            exactR += R
        elif C < X:
            sumrl += R
            sumrcl += R*C
        else:
            sumrh += R
            sumrch += R*C


    if DEBUG: print >> sys.stderr, 'exactR, sumrcl, sumrl, sumrch, sumrh', exactR, sumrcl, sumrl, sumrch, sumrh

    if exactR != 0:
        res = V / exactR
    else:
        res = 10e8

    if DEBUG: print >> sys.stderr, 'res', res

    if sumrl == 0 or sumrh == 0:
        if exactR != 0:
            print("%.9f" % float(res) )
        else:
            print 'IMPOSSIBLE'
    else:
        rl, rh = sumrl, sumrh
        cl, ch = sumrcl / sumrl, sumrch / sumrh

        tl = V * (X - cl) / (rh * (ch - cl))
        th = V * (X - ch) / (rl * (cl - ch))

        res = min(res, max(tl, th))

        if DEBUG: print >> sys.stderr, 'mixing', res

        if exactR != 0:
            rl, rh = sumrl + exactR, sumrh
            cl, ch = (sumrcl + X*exactR) / sumrl, sumrch / sumrh

            tl = V * (X - cl) / (rh * (ch - cl))
            th = V * (X - ch) / (rl * (cl - ch))

            res = min(res, max(tl, th))

            if DEBUG: print >> sys.stderr, 'adding to cool', res

            rl, rh = sumrl, sumrh + exactR
            cl, ch = sumrcl / sumrl, (sumrch + X*exactR ) / sumrh

            tl = V * (X - cl) / (rh * (ch - cl))
            th = V * (X - ch) / (rl * (cl - ch))

            res = min(res, max(tl, th))

            if DEBUG: print >> sys.stderr, 'adding to hot', res

        print("%.9f" % float(res) )


