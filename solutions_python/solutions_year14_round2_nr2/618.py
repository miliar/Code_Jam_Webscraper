for tc in xrange(1, input() + 1):
    A, B, K = map(int, raw_input().split())
    ans = 0
    for a in xrange(A):
        for b in xrange(B):
            if (a & b) < K:
                ans += 1
    print "Case #{}: {}".format(tc, ans)
