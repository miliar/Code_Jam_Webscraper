#!/usr/bin/env python
"""
Recycled numbers

Google Code Jam
2012 Qual Round
Problem C: Recycled numbers


Author: Kelsey Jordahl <kajord@gmail.com>
Time-stamp: <Sat Apr 14 18:21:42 EDT 2012>

"""

import sys
from numpy import *

verbose = False
debug = False

def recycled(A, B):
    d = {}
    s = set()
    for n in xrange(A, B + 1):
        k = tuple(sorted(str(n)))
        if d.get(k) is None:
            d[k] = [n]
        else:
            d[k].append(n)
    for k, l in d.iteritems():
        if len(l) > 1:
            # we have at least one permutation
            for i, n in enumerate(l):
                for m in l[i+1:]:
                    N = str(n)
                    M = str(m)
                    for j in xrange(1, len(N)):
                        if N[j:] + N[:j] == M:
                            if verbose:
                                print N, M, j
                            t = tuple(sorted([n, m]))
                            s.add(t)
    return len(s)


def main():
    if len(sys.argv) < 2:
        infile = 'C-test.in'
    else:
        infile = sys.argv[1]
    if len(sys.argv) < 3:
        if infile[-3:] == '.in':
            outfile = infile[:-3] + '.out'
        else:
            outfile = infile + '.out'
    else:
        outfile = sys.argv[2]
    if verbose:
        print 'infile %s, outfile %s' % (infile, outfile)
    f = open(infile)
    o = open(outfile,'w')
    T = int(f.readline())
    print 'T = %d' % T
    for i in range(0, T):
        line = f.readline().strip()
        A, B = [int(s) for s in line.split()]
        o.write('Case #%d: %s\n' % (i+1, recycled(A, B)))
    f.close
    o.close

if __name__ == '__main__':
    main()
