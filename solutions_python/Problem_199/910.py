#!/usr/bin/env python


def flip(state, index, K):
    return state[:index] + ''.join({'-': '+', '+': '-'}[a] for a in state[index:index+K]) + state[index+K:]


def solve(state, K):
    if '-' not in state:
        return 0
    S = len(state)
    seen = set([state])
    states = set([state])
    turns = 0
    while True:
        turns = turns + 1
        newstates = set([])
        for cstate in states:
            for i in range(S - K + 1):
                cand = flip(cstate, i, K)
                if '-' not in cand:
                    return turns
                if cand in seen:
                    continue
                newstates.add(cand)
                seen.add(cand)
        if len(newstates) == 0:
            return 'IMPOSSIBLE'
        states = newstates

T = int(raw_input().strip())
for t in range(T):
    state, K = raw_input().strip().split()
    K = int(K)
    print 'Case #%d: %s' % (t+1, solve(state, K))
