def solve(S, K):
    c = 0
    S = list(S)
    for i in range(len(S)-K+1):
        if S[i] == '+': continue
        c += 1
        for j in range(K):
            S[i+j] = '-' if S[i+j] == '+' else '+'

    minus = sum(1 for s in S if s == '-')
    return c if minus == 0 else 'IMPOSSIBLE'

import sys
sys.stdin = open('A-large.in', 'rt')
sys.stdout = open('A-large.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    S, K = raw_input().strip().split(' ')
    print "Case #%d: %s" % (t, solve(S, int(K)))
