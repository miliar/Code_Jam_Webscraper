import math

with open('a.out', 'w') as fl:
    t = int(input())
    for case in range(t):
        D, N = map(int, input().split())
        t = 0
        for i in range(N):
            k, s = map(int, input().split())
            t = max(t, (D-k)/s)

        print('Case #{0}:'.format(case + 1), D / t, file=fl)

