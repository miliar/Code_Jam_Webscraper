def solve(S):
    p = 0
    for i in range(len(S)-1):
        if S[i] > S[i+1]:
            S = S[:p] + str(int(S[p]) - 1) + ('9'*(len(S)-p-1))
            break

        if S[i] < S[i+1]:
            p = i+1

    return S.lstrip('0')

import sys
sys.stdin = open('B-large.in', 'rt')
sys.stdout = open('B-large.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    S = raw_input().strip()
    print "Case #%d: %s" % (t, solve(S))
