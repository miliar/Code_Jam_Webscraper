import sys

fin = iter(open(sys.argv[1], 'r') if len(sys.argv) == 2 else sys.stdin)
T = int(next(fin).strip())
for t in xrange(T):
    N = int(next(fin).strip())
    A = map(int, next(fin).strip().split())
    assert len(A) == N

    count = 0
    while A:
        min_val, min_index = min((v, i) for i, v in enumerate(A))
        count += min(min_index, len(A) - min_index - 1)
        del A[min_index]

    print 'Case #%d: %d' % (t+1, count)
