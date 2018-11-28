# Zolmeister

import math

T = int(raw_input())

def sort(pancakes):
    return sorted(pancakes, key=lambda x: (x[1] * x[0]), reverse=True)

def count(pancakes):
    r = pancakes[0][0]
    top = math.pi * r ** 2
    sides = 0
    for r, h in pancakes:
        sides += 2 * math.pi * r * h
    return sides + top

for t in xrange(T):
    N, K = map(int, raw_input().split())
    pancakes = []
    for l in xrange(N):
        pancakes.append(map(int, raw_input().split()))

    maxx = 0
    pancakes = sort(pancakes)
    for i, pancake in enumerate(pancakes):
        rest = pancakes[:i] + pancakes[i + 1:]
        maxx = max(count([pancake] + rest[:K - 1]), maxx)

    s = '{0:.10f}'.format(maxx)
    print 'Case #{}: {}'.format(t + 1, s)
