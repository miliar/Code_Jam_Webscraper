from collections import Counter
from fileinput import input
from math import pi


def surface(pancakes):
    (radius, _) = pancakes[0]
    return pi * radius * radius + sum([2 * pi * r * h for (r, h) in pancakes])


def combinations(pancakes, select_count):
    if select_count == 1:
        return [[p] for p in pancakes]

    combs = []
    for i, p in enumerate(pancakes[:-select_count+1]):
        remaining = pancakes[i + 1:]
        for comb in combinations(remaining, select_count - 1):
            combs.append([p] + comb)

    return combs


lines = input()
problems = int(lines.readline())
for index in range(1, problems + 1):

    total, select = map(int, lines.readline().split())
    pancakes = list()

    for _ in range(total):
        radius, height = map(int, lines.readline().split())
        pancakes.append((radius, height))

    pancakes = list(reversed(sorted(pancakes, key=lambda p: p[0])))
    combs = combinations(pancakes, select)
    best = max(combs, key=surface)

    print(f'Case #{index}: {surface(best)}')
