#!/usr/bin/env python3
T = int(input())
for t in range(T):
    N = input()
    k = 0
    s = 0
    for i, v in enumerate(N):
        v = int(v)
        if v > k:
            s = i
            k = v
        elif v < k:
            ans = N[:s] + str(int(N[s]) - 1) + "9" * (len(N) - s - 1)
            break
    else:
        ans = N
    print("Case #{}: {}".format(t + 1, ans.lstrip("0")))
