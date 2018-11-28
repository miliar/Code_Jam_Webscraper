#!/usr/bin/env python3
T = int(input())
for t in range(T):
    ans = 0
    S, K = input().split()
    K = int(K)
    S = [int(c + '1') for c in S]
    l = len(S) - K + 1
    for i in range(l):
        if S[i] == -1:
            ans += 1
            S[i:i+K] = [-s for s in S[i:i+K]]
    if any(s != 1 for s in S):
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(t + 1, ans))
