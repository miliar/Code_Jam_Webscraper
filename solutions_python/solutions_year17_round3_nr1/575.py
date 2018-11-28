from math import pi
from itertools import combinations


def solve(n, k, pancakes):
    bases = sorted(pancakes, key=lambda x: (-x[0], -x[0]*x[1]))
    pancakes = sorted(pancakes, key=lambda x: (-x[0]*x[1]))
    #print(pancakes)
    c = tuple()
    best = 0
    for base in bases:
        top = base[0] * base[0] + 2 * base[0] * base[1]

        rest = 2 * sum(a * b for a, b in pancakes[:k-1])
        if base in pancakes[:k-1]:
            rest += (2 * pancakes[k-1][0] * pancakes[k-1][1]) - (2 * base[0] * base[1])

        if top + rest > best:
            best = top + rest
            c = [base] + pancakes[:k-1]
    ys = [(p[0], p[1], p[0]*p[1]) for p in pancakes]
    return pi * best


for t in range(int(input())):
    n, k = map(int, input().split())
    pancakes = [tuple(map(int, input().split())) for _ in range(n)]
    ans = solve(n, k, pancakes)
    print("Case #{}: {}".format(t+1, ans))