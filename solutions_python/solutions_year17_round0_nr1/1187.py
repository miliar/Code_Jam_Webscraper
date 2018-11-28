
def solve(t):
    S, K = raw_input().split()
    S = [c == '+' for c in S]
    K = int(K)

    ans = 0
    for i in xrange(len(S)-K+1):
        if not S[i]:
            ans += 1
            for j in xrange(i, i+K):
                S[j] ^= True
    for i in xrange(len(S)-K+1, len(S)):
        if not S[i]:
            ans = -1

    if ans == -1:
        print 'Case #%d: IMPOSSIBLE' % t
    else:
        print 'Case #%d: %d' % (t, ans)

T = input()
for i in xrange(T):
    solve(i+1)
