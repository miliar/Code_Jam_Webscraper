import sys

toks = sys.stdin.read().split()
toks.reverse()

T = int(toks.pop())
for i in xrange(T):
    S = [ch == '+' for ch in toks.pop()]
    K = int(toks.pop())

    flips = 0
    for j in xrange(len(S) - K + 1):
        if not S[j]:
            flips += 1
            for k in xrange(j, j + K):
                S[k] = not S[k]

    if not all(S):
        print 'Case #{}: IMPOSSIBLE'.format(i+1)
    else:
        print 'Case #{}: {}'.format(i+1, flips)
