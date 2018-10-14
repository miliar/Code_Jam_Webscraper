import sys
def find_flips(s, K):
    if sum(s) == len(s):
        return 0
    if sum(s) == len(s) - 1:
        return -1
    #if len(s) <= K:
    #    return -1

    first_zero = 2**32 # int max
    for i, x in enumerate(s):
        if x == 0:
            first_zero = i
            break

    if first_zero + K <  len(s):
        for i in xrange(K):
            s[first_zero + i] = 1 if s[first_zero + i] == 0 else 0
    else:
        for i in xrange(K):
            s[len(s) - K + i] = 1 if s[len(s) - K + i] == 0 else 0
        if sum(s[first_zero:]) != len(s[first_zero:]):
            return -1

    next_flip = find_flips(s, K)
    if next_flip == -1:
        return next_flip
    else:
        return next_flip + 1

sin = sys.stdin
nt = int(sin.readline().strip())
for i in xrange(nt):
    S, K = sin.readline().strip().split(' ')
    s = [0] * len(S)
    for j, c in enumerate(S):
        s[j] = 1 if c == '+' else 0
    flips = find_flips(s, int(K))
    print 'Case #{0}: {1}'.format((i+1), 'IMPOSSIBLE' if flips == -1 else flips)

