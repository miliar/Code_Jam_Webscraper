def solve(N, K):
    if N == K:
        return (0, 0)

    depth = 0
    low = high = N
    while not 2 ** depth <= K < 2 ** (depth + 1):
        depth += 1
        low = (low - 1) // 2
        high = high // 2
    if low == high:
        nlow = 2 ** depth
    else:
        nlow = ((high + 1) * 2 ** depth - N - 1) // (high - low)
    nhigh = 2 ** depth - nlow
    assert nlow * low + nhigh * high + 2 ** depth - 1 == N
    i = K - 2 ** depth
    x = high if i < nhigh else low
    if x <= 1:
        return (0, 0)
    return (x // 2, (x - 1) // 2)


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    print('Case #{}: {} {}'.format(tc + 1, *solve(N, K)))
