#! /usr/bin/python

import os
import sys
import copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')


T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    debug(' ************* case %s' % t)
    [D, N] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    time_needed = 0
    for i in range(N):
        [K_i, S_i] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        time_needed_i = (D - K_i) / float(S_i)
        if time_needed_i > time_needed:
            time_needed = time_needed_i
    ret = D / time_needed
    sys.stdout.write('Case #%s: %.6f\n' % (t, ret))
