from math import ceil

T = int(input())

for t in range(1, T + 1):
    (C, F, X) = tuple(map(float, input().split(' ')))
    
    N = ceil((F * X - 2 * C) / (F * C) - 1)
    if N < 0: N = 0

    time = sum(C / (2 + i * F) for i in range(0, N))
    time += X / (2 + N * F)

    print('Case #%d: %.7f' % (t, time))

