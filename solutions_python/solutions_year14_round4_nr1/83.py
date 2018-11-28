import sys

fin = iter(open(sys.argv[1], 'r') if len(sys.argv) == 2 else sys.stdin)
T = int(next(fin).strip())
for t in xrange(T):
    N, X = map(int, next(fin).strip().split())
    S = map(int, next(fin).strip().split())
    assert len(S) == N

    S = sorted(S)
    count = 0
    while S:
        rem = X - S.pop()
        for i, y in enumerate(S):
            if y > rem:
                if i > 0:
                    del S[i-1]
                break
        else:
            if S:
                S.pop()
        count += 1
    print 'Case #%d: %d' % (t+1, count)
