from collections import namedtuple
from decimal import Decimal


cases = int(input())
for case in range(1, cases + 1):
    D, N = map(int, input().split())
    hs = []
    for n in range(N):
        k, s = map(int, input().split())
        hs.append(Decimal((D - k) / s))

    max_h = max(hs)
    print('Case #{}: {:.6f}'.format(case, D / max_h))





"""
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10

"""