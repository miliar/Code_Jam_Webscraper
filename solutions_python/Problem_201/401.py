T = int(input())
for t in range(1, T + 1):
    N, K = [int(_) for _ in input().split()]
    k = 0
    s = 0
    while s < K:
        s += 2 ** k
        k += 1
    order = K - (2 ** (k - 1) - 1) - 1
    big = (N - (2 ** (k - 1) - 1)) % (2 ** (k - 1))
    num = (N - (2 ** (k - 1) - 1)) // (2 ** (k - 1))
    # print('level: %d, order: %d, big ones: %d, num is: %d' % (k, order, big, num))
    ans = [0, 0]
    if order < big:
        num += 1
    if num % 2 == 1:
        ans = [num // 2, num // 2]
    else:
        ans = [num // 2, num // 2 - 1]
    print('Case #%d: %d %d' % (t, ans[0], ans[1]))
