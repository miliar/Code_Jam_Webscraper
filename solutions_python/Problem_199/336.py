# -*- coding: utf-8 -*-
T = int(raw_input())

for case in xrange(1, T + 1):
    S, K = raw_input().split()
    K = int(K)
    S = list(S)
    N = len(S)
    ans = 0
    for i in xrange(N - K + 1):
        if S[i] == "-":
            ans += 1
            for j in xrange(i, i + K):
                S[j] = "+" if S[j] == "-" else "-"
    if "-" in S:
        ans = "Impossible"
    print "Case #%s: %s" % (case, ans)
