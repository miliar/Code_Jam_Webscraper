T = int(input())

for t in range(T):
    N, K = map(int, input().split())

    d = {N: 1}
    while d[N] < K:
        if N % 2 == 0:
            d.setdefault(N // 2, 0)
            d[N // 2] += d[N]
            d.setdefault(N // 2 - 1, 0)
            d[N // 2 - 1] += d[N]
        else:
            d.setdefault(N // 2, 0)
            d[N // 2] += 2 * d[N]
        K -= d[N]
        del d[N]
        N = max(d.keys())

    print("Case #{}: {} {}".format(
        t+1,
        N // 2, N // 2 - 1 if N % 2 == 0 else N // 2
    ))
