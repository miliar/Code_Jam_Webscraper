# Zolmeister

T = int(raw_input())

for t in xrange(T):
    S, K = raw_input().split()
    K = int(K)
    SS = map(lambda c: 1 if c == '+' else 0, S)
    i = 0
    flips = 0

    while i < len(SS):
        while i < len(SS) and SS[i] == 1:
            i += 1
        if i > len(SS) - K:
            break
        for j in xrange(i, i + K):
            SS[j] = 1 if SS[j] == 0 else 0
        flips += 1
        i += 1

    if 0 in SS:
        flips = 'IMPOSSIBLE'
    print 'Case #{}: {}'.format(t + 1, flips)
