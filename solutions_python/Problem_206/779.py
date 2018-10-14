import math

n = int(raw_input())

for i in range(1, n + 1):
    D, N = [int(x) for x in raw_input().split(' ')]

    max_time = -1
    for _ in range(N):
        K, S = [int(x) for x in raw_input().split(' ')]

        max_time = max((D - K) * 1.0 / S, max_time)

    ans = D / max_time

    print("Case #{}: {}".format(i, ans))
