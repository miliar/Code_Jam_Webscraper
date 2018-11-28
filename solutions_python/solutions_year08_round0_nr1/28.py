cases = int(raw_input())
for case in xrange(cases):
    S = int(raw_input())
    engines = [raw_input() for _ in xrange(S)]

    Q = int(raw_input())
    q = [raw_input() for _ in xrange(Q)]

    dp = [[2**31] * S for _ in xrange(Q)]

    if len(q) == 0:
        res = 0
    else:
        for i in xrange(S):
            dp[0][i] = 0 if engines[i] != q[0] else 2**31


        for i in xrange(1, Q):
            for j in xrange(S):
                dp[i][j] = 1 + min([dp[i-1][k] for k in xrange(S) if k != j])
                if q[i] != engines[j]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])

        res = min(dp[Q-1][k] for k in xrange(S))

    print 'Case #%d: %d' % (case+1, res)
