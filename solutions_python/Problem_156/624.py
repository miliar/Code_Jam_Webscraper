import math
import sys

sys.stdin = open('B-large.in')
sys.stdout = open('B-large.out', 'w')

T = int(input())
for ti in range(1, T + 1):
    D = int(input())
    P = list(map(int, input().split()))
    P.sort(reverse=True)

    minutes = 1000
    for i in range(1, max(P) + 1):
        special = 0
        for p in P:
            if p > i:
                special += math.ceil(p / i) - 1
        minutes = min(minutes, special + i)

    print('Case #{}: {}'.format(ti, minutes))
