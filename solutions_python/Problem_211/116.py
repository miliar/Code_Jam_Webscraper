T = input()
for t in range(T):
    N, K = map(int, raw_input().split())
    U = input()
    P = map(float, raw_input().split())

    P.sort()

    i = 0
    while i < K - 1 and U > 0:
        if P[i + 1] != P[i]:
            r = (P[i + 1] - P[i]) * (i + 1)
            if r <= U:
                U -= r
                for j in range(i + 1):
                    P[j] += P[i + 1] - P[i]
            else:
                for j in range(i + 1):
                    P[j] += U / (i + 1)
                U = 0
        i += 1

    for i in range(K):
        P[i] = min(1, P[i] + U / K)

    res = reduce(lambda x, y: x * y, P, 1)
    print 'Case #%d: %lf' % (t + 1, res)
