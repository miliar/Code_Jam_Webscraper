#! /usr/bin/python

import os
import sys
import copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

def solve(S, K):
    count = 0
    lenS = len(S)
    debug('*         : S=%s' % ''.join(S))
    for i, x in enumerate(S):
        debug('i=%s, x=%s' % (i,x))
        if lenS - i == K and '-' in S[i:] and '+' in S[i:]:
            return 'IMPOSSIBLE'
        if lenS - i == K and '-' in S[i:]:
            return count+1
        if lenS - i == K:
            return count
        if x == '+':
            continue
        if x == '-':
            count += 1
            for j in range(K):
                if S[i+j] == '-':
                    S[i+j] = '+'
                else:
                    S[i+j] = '-'
            debug('* counting: S=%s' % ''.join(S))
    return count

sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    debug(' ************* case %s' % t)
    [S, K] = sys.stdin.readline().strip().split(' ')
    K = int(K)
    S = list(S)
    ret = solve(S, K)
    sys.stdout.write('Case #%s: %s\n' % (t, ret))
