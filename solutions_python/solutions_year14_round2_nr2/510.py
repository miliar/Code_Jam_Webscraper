#!/usr/bin/env python3


T = int(input())
for t in range(1,T+1):
    A, B, K = list(map(int, input().split()))
    answer = 0
    for x in range(A):
        for y in range(B):
            if x & y < K:
                answer += 1

    print("Case #%d: %s" % (t, answer))
