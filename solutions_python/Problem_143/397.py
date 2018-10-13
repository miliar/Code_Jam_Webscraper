def solve_stupid(A, B, K):
    res = 0
    for a in xrange(0, A):
        for b in xrange(0, B):
            if (a & b) < K:
                res += 1
    return res

T = int(raw_input())
for t in xrange(0, T):
    (A, B, K) = map(int, raw_input().split())
    print "Case #%d: %d" % (t + 1, solve_stupid(A, B, K))
