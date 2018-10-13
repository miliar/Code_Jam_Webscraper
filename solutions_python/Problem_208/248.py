def solve(N, Q, E, S, D, U, K):
    if Q != 1:
        return None

    dist = [0]
    for i in range(1, N):
        dist.append(dist[i - 1] + D[i - 1][i])

    ts = [10 ** 100] * N
    ts[N - 1] = 0
    for pos in range(N - 1, 0, -1):
        for i in range(pos):
            d = dist[pos] - dist[i]
            if d <= E[i]:
                ts[i] = min(ts[i], ts[pos] + d / S[i])
    return ts[0]


T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    E, S = [], []
    for _ in range(N):
        e, s = map(int, input().split())
        E.append(e)
        S.append(s)
    D = []
    for _ in range(N):
        D.append(list(map(int, input().split())))
    U, K = [], []
    for _ in range(Q):
        u, k = map(int, input().split())
        U.append(u)
        K.append(k)
    print('Case #{}: {}'.format(tc + 1, solve(N, Q, E, S, D, U, K)))
