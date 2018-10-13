
def solve(t):
    N, C, M = map(int, raw_input().split())
    S = [[0, 0] for i in xrange(N)]
    for i in xrange(M):
        p, b = map(int, raw_input().split())
        p -= 1
        b -= 1
        S[p][b] += 1

    ans = 0

    for i in xrange(N):
        for j in xrange(i+1, N):
            mn = min(S[i][0], S[j][1])
            ans += mn
            S[i][0] -= mn
            S[j][1] -= mn
    for i in xrange(N):
        for j in xrange(i+1, N):
            mn = min(S[i][1], S[j][0])
            ans += mn
            S[i][1] -= mn
            S[j][0] -= mn

    ans2 = 0

    for i in xrange(1, N):
        if S[i][0] > 0 and S[i][1] > 0:
            mn = min(S[i][0], S[i][1])
            ans += mn
            ans2 += mn
            S[i][0] -= mn
            S[i][1] -= mn

    for i in xrange(N):
        ans += S[i][0] + S[i][1]

    print "Case #%d: %d %d" % (t, ans, ans2)


T = int(raw_input())
for i in xrange(T):
    solve(i+1)
