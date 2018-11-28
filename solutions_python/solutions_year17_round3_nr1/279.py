#! /usr/bin/python

import os
import sys
import copy
import math

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

def solve(pancakes, K):
    pancakes.sort()
    pancakes.reverse()
    best = 0
    for i in range(len(pancakes)):
        debug('trying i=%s' % i)
        if i > N - K:
            break
        my_run = (pancakes[i][0]*pancakes[i][0]) + pancakes[i][1] * pancakes[i][0] * 2
        debug(' ***  a=%s (%s) %s' % (my_run, pancakes[i], my_run))
        pancakes_rest = list(reversed(sorted(pancakes[i+1:], key=lambda x: x[0]*x[1])))
        for j in range(K-1):
            debug(' ** adding j=%s' % j)
            my_run += pancakes_rest[j][1] * pancakes_rest[j][0] * 2 
        debug(' * my_best = %s' % my_run)
        if my_run > best:
            best = my_run
    return best * math.pi

sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    debug(' ************* case %s' % t)
    pancakes = []
    [N, K] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    for i in range(N):
        [R_i, H_i] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        pancakes.append((R_i, H_i))
    ret = solve(pancakes, K)
    sys.stdout.write('Case #%s: %.6f\n' % (t, ret))
