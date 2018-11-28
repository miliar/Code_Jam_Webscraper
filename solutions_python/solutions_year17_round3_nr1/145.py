import math

T = input()
for t in range(T):
    N, K = map(int, raw_input().split())

    cakes = [map(int, raw_input().split()) for n in range(N)]
    cakes = [(r, h, 2 * r * h) for r, h in cakes]
    cakes.sort()

    expose = 0
    for k in range(K - 1, N):
        available = [e for r, h, e in cakes[:k]]
        available.sort(reverse = True)

        if sum(available[:K - 1]) + cakes[k][0] ** 2 + cakes[k][2] > expose:
            expose = sum(available[:K - 1]) + cakes[k][0] ** 2 + cakes[k][2]

    print 'Case #%d: %lf' % (t + 1, math.pi * expose)
