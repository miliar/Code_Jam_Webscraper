#! /usr/bin/python

import os, sys, copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

def solve_2(V, X, R, C):
    if max(C) < X or min(C) > X:
        debug('max-min')
        return None
    t1 = (X - C[0]) * V / (R[1] * (C[1] - C[0]))
    t0 = (V - R[1]*t1) / R[0]
    return max(t0, t1)
            
T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    [N, V, X] = [float(x) for x in(sys.stdin.readline().split(' '))]
    C = []
    R = []
    ret = None
    for i in range(int(N)):
        r, c = [float(x) for x in(sys.stdin.readline().split(' '))]
        C.append(c)
        R.append(r)
    debug('%s' % [N, V, X])
    debug('%s' % [R, C])
    if N == 1:
        if C[0] == X:
            ret = V / R[0]
        else:
            ret = None
    elif N == 2 and C[0] == C[1] and C[0] == X:
        ret = V / (R[0] + R[1])
    elif N == 2:
        ret = solve_2(V, X, R, C)
    if ret is None:
        sys.stdout.write('Case #%s: IMPOSSIBLE\n' % (t,))
    else:
        sys.stdout.write('Case #%s: %.6f\n' % (t, ret))
        
