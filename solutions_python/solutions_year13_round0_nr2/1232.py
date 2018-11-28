

def solve(F):
    R = map(max, F)
    C = map(max, zip(*F))
    for r in xrange(len(F)):
        for c in xrange(len(F[r])):
            if not (R[r] <= F[r][c] or C[c] <= F[r][c]):
                return 'NO'
    return 'YES'

T = int(raw_input())
for t in xrange(T):
    N, M = map(int, raw_input().split())
    F = [map(int,raw_input().split()) for i in xrange(N)]


    print 'Case #%d: %s' % (t+1, solve(F))