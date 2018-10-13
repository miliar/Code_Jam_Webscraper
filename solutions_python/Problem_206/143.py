from __future__ import division
import sys

toks = open(sys.argv[1], 'r').read().split()
toks.reverse()

T = int(toks.pop())
for i in xrange(T):
    D = int(toks.pop())
    N = int(toks.pop())

    horses = []
    for j in xrange(N):
        K = int(toks.pop())
        S = int(toks.pop())
        horses.append((K, S))

    horses.sort(key=lambda h: h[0], reverse=True)

    cur = 0
    next = 1

    while next < len(horses):
        K1, S1 = horses[cur]
        K2, S2 = horses[next]

        if S1 >= S2:
            cur = next
        else:
            intersect = K1 + S1*((K2-K1) / (S1 - S2))
            if intersect > D:
                cur = next
        next += 1

    K, S = horses[cur]
    r = D * (S / (D-K))

    print 'Case #{}: {}'.format(i+1, r)
