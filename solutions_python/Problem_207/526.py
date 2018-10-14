#!/usr/bin/env python

import re

# Solving the simple
def solve(N, R, O, Y, G, B, V):
    cnt = min(R, Y, B)
    state = 'RYB' * cnt
    R = R - cnt
    Y = Y - cnt
    B = B - cnt

    if R == 0:
        cnt = min(Y, B)
        state += 'YB' * cnt
        Y = Y - cnt
        B = B - cnt
    elif Y == 0:
        cnt = min(R, B)
        state += 'RB' * cnt
        R = R - cnt
        B = B - cnt
    else:
        cnt = min(R, Y)
        state += 'RY' * cnt
        R = R - cnt
        Y = Y - cnt

    if state == '':
        state = '*'
    else:
        state = state + state[0]

    for _ in range(R):
        nstate = re.sub(r'([^R])([^R])', '\\1R\\2', state, 1)
        if state == nstate:
            return 'IMPOSSIBLE'
        state = nstate
    for _ in range(Y):
        nstate = re.sub(r'([^Y])([^Y])', '\\1Y\\2', state, 1)
        if state == nstate:
            return 'IMPOSSIBLE'
        state = nstate
    for _ in range(B):
        nstate = re.sub(r'([^B])([^B])', '\\1B\\2', state, 1)
        if state == nstate:
            return 'IMPOSSIBLE'
        state = nstate

    state = state[1:]
    return state


T = int(raw_input().strip())
for t in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in raw_input().strip().split()]
    res = solve(N, R, O, Y, G, B, V)
    print 'Case #%d: %s' % (t+1, res)
