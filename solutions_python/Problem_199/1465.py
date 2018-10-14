"""
Oversized Pancake Flipper
"""

cake = ['-', '+']

output = 'Case #%d: %s'

T = int(raw_input().strip())

for t in xrange(1, T+1):
    S, K = raw_input().strip().split()
    K = int(K)
    flips = 0
    for i in xrange(len(S)-K+1):
        if S[i] == cake[0]:
            flips += 1
            for j in xrange(i, i+K):
                index = cake.index(S[j])
                S = S[:j] + cake[1-index] + S[j+1:]

    _out = 'IMPOSSIBLE' if cake[0] in S[len(S)-K+1:] else str(flips)
    print output % (t, _out)
