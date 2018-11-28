#!/usr/bin/env python

T = int(input())

for t in range(1, T + 1):
    S, n = input().split()
    N = len(S)
    n = int(n)

    flip_cnt = [0] * N
    for i, s in enumerate(S):
        if s == '-' :
            flip_cnt[i] = 1
    # print(flip_cnt)

    cnt = 0
    for i in range(0, N - n + 1):
        if flip_cnt[i] == 1:
            cnt += 1
            for j in range(i, i + n):
                if flip_cnt[j] == 1:
                    flip_cnt[j] = 0
                else:
                    flip_cnt[j] = 1

    if any(flip_cnt):
        ans = "IMPOSSIBLE"
    else:
        ans = cnt
    print("Case #{}: {}".format(t, ans))
