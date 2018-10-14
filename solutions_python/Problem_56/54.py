#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

import numpy
import sys
from itertools import chain

def read_numbers(input):
    return [ int(x) for x in input.readline().strip().split() ]

def find_things(map, N, K):
    # trans is a transposed version of map
    trans = [ ''.join(line[i] for line in map) for i in xrange(N) ]

    # Diagonals
    diag1 = [ ''.join(map[    i][off-i] for i in xrange(off+1) if 0<=i<N and 0<=off-i<N) for off in xrange(N+N-1) ]
    diag2 = [ ''.join(map[N-1-i][off-i] for i in xrange(off+1) if 0<=i<N and 0<=off-i<N) for off in xrange(N+N-1) ]

    #print '\n'.join(map)
    #print '\n'.join(trans)
    #print '\n'.join(diag1)
    #print '\n'.join(diag2)

    blue = 'B'*K
    red  = 'R'*K

    has_blue = any(blue in line for line in chain(map, trans, diag1, diag2))
    has_red  = any(red  in line for line in chain(map, trans, diag1, diag2))

    if has_red and has_blue:
        return 'Both'
    elif has_red:
        return 'Red'
    elif has_blue:
        return 'Blue'
    else:
        return 'Neither'


def main(input):
    testcases = int(input.readline().strip())
    for testcase in xrange(testcases):
        # N = size
        # K = connect-K
        N, K = read_numbers(input)

        # Reading input
        map = [input.readline().strip() for i in xrange(N)]
        # Gravity to the right
        map2 = [ line.replace('.', '').rjust(N, '.') for line in map ]

        print "Case #%d: %s" % (testcase+1, find_things(map2, N, K))

if __name__ == '__main__':
    main(sys.stdin)
