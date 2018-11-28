def do(N, K):
    if K == N:
        return 0, 0

    n = N - 1
    a = n // 2
    b = n - a

    k = K - 1
    ka = k // 2
    kb = k - ka

    if K == 1:
        return b, a

    if K == 2:
        return do(b, 1)

    if n % 2 == 0:
        return do(b, kb)
    else:
        return do(a, ka) if k % 2 == 0 else do(b, kb)

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T + 1):
        N, K = [int(x) for x in input().split(' ')]
        mx, mn = do(N, K)
        print('Case #{}: {} {}'.format(i, mx, mn))
