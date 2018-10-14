#!/usr/bin/env python

import sys, fractions, itertools
from bisect import bisect

F = fractions.Fraction
cwr = itertools.combinations_with_replacement

POWERS = [1, 2]
for i in xrange(40):
    POWERS.append(2 * POWERS[-1])

def main(in_stream, out_stream):
    n_cases = int(in_stream.next())
    for i in xrange(1, n_cases+1):
        target = F(in_stream.next())
        num, den = target.numerator, target.denominator
        try:
            idx = 1 + POWERS.index(den)
            res = idx - bisect(POWERS, num)
        except ValueError:
            res = 'impossible'
        out_stream.write('Case #%d: %s\n' % (i, res))

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
