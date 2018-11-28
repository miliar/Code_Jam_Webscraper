def solve(D, N, K, S):
    maxt = 0
    for i in range(N):
        t = (D - K[i]) / S[i]
        maxt = max(maxt, t)
    return D / maxt


T = int(input())
for tc in range(T):
    D, N = map(int, input().split())
    K, S = [], []
    for _ in range(N):
        k, s = map(int, input().split())
        K.append(k)
        S.append(s)
    print('Case #{}: {:.6f}'.format(tc + 1, solve(D, N, K, S)))
