prefix = "Case #%d:"
T = input()
for t in xrange(1, T+1):
    S, K = raw_input().split()
    S = [(0, 1)[a=="+"] for a in S]
    N = len(S)
    K = int(K)
    ans = 0
    for i in xrange(N - K + 1):
        if S[i] == 0:
            ans += 1
            for j in xrange(K):
                S[i+j] ^= 1
    print prefix%t,
    print ans if all(c for c in S) else "IMPOSSIBLE"
