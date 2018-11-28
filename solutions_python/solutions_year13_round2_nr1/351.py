#!/usr/bin/python

import logging
import math
import os
import sys

fin = sys.stdin

msg_c = 'Case #%d: %s'

def num_to_add(m1, m2):
    num = math.ceil( \
            math.log( \
                (m2 - 1) \
                / (m1 - 1) ) \
            / math.log(2) )
    num = int(num)
    a = (2 ** num) * (m1 - 1) + 1
    # Verify (might hit boundary condition where m1 now equals m2)
    while a <= m2:
        # Add one more mote
        num += 1
        a = a * 2 - 1
    # Absorb m2
    a += m2
    logging.debug('num_to_add: %d, %d => %d, %d' % (m1, m2, a, num))
    return (a, num)

def solve(fin):
    A, N = map(int, fin.readline().strip().split())
    M = map(int, fin.readline().strip().split())
    logging.debug('A: %d' % A)

    if A < 2:
        return str(N)
    M.sort()
    logging.debug('M: %s' % str(M))

    count = 0
    count_add = 0
    count_rem = 0
    while len(M) > 0:
        # shift smallest value off
        m = M[0]
        del M[0]
        if A > m:
            A += m
            # Check to see if we are removing entries
            if count_rem > 0:
                count_rem += 1
                if count_rem >= count_add:
                    count += count_add
                    count_add = 0
                    count_rem = 0
            continue
        A, cnt = num_to_add(A, m)
        count_add += cnt
        count_rem += 1
        if count_add <= count_rem:
            count += count_add
            count_add = 0
            count_rem = 0
    # If this count > 0, that means we had to remove some,
    # but not as many as we would've had to add
    if count_rem > 0:
        return str(count + count_rem)
    return str(count)

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        print msg_c % (t, solve(fin))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
