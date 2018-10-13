#! /usr/bin/python

import os
import sys
import copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

def solve(N):
    previous = 0
    for i, x in enumerate(N):
        if x > previous:
            previous = x
            offset = i
            debug('previous = %s, offset = %s' % (previous, offset))
            continue
        if x == previous:
            debug('previous = %s, offset = %s' % (previous, offset))
            continue
        if x < previous:
            debug('%s | %s | %s | %s' % (
                i, N[0:offset], str(int(N[offset])-1), '9' * (len(N) - offset - 1)))
            return int(N[0:offset] + str(int(N[offset])-1) + '9' * (len(N) - offset - 1))
    return N

sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    debug(' ************* case %s' % t)
    N = sys.stdin.readline().strip()
    ret = solve(N)
    sys.stdout.write('Case #%s: %s\n' % (t, ret))
