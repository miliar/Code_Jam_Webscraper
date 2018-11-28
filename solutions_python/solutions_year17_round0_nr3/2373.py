#!/usr/bin/python

import sys
import fileinput
import string

def getsize(s):
    if s % 2:
        return ((s-1)//2, (s-1)//2)
    else:
        return (s//2, (s-1)//2)

def solve(n, k):
    parts = 1
    while parts * 2 <= k:
        parts *= 2

    remaining = n-parts
    k -= parts

    lower_size = remaining // parts
    num_above = remaining % parts

    if k <= num_above:
        return getsize(lower_size + 1)
    else:
        return getsize(lower_size)

if __name__ == '__main__':
    input = fileinput.input()
    T = int(input.next().strip())

    for tcase in xrange(T):
        print 'Case #%d:' % (tcase + 1),

        n, k = map(int, input.next().split())
        print '%s %s' % solve(n, k)
