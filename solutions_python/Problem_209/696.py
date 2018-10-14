import os
import re
import sys
import math
import time
import bisect
import random
import datetime
import itertools
import functools
import collections


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def solve():
    nb = int(input())

    debug("[START] %d cases to solve:" % nb)

    total = 0

    for i in range(1, nb + 1):
        print("Case #%d:" % i, end=" ")

        start = time.process_time()
        solve_case()
        end = time.process_time()

        t = end - start
        total += t

        m, s = divmod(total, 60)

        debug("[%d:%02.02f] Case #%d solved in %.02f seconds" % (m, s, i, t))

    debug("[END] All cases solved")


def area(r):
    return math.pi * r * r

def border(r, h):
    return 2 * math.pi * r * h

def syrup(pancakes):
    surface = 0
    prev_r = 0
    for r, h in reversed(pancakes):
        covered = area(r) - area(prev_r) + border(r, h)
        surface += covered
        prev_r = r
    return surface

def solve_case():
    n, k = map(int, input().split())
    pancakes = []
    for _ in range(n):
        r, h = map(int, input().split())
        pancakes.append((r, h))
    pancakes.sort(reverse=True)

    candidates_per_size = {i: [] for i in range(k)}
    candidates_per_size[0].append([])
    best = -1
    idx = 0

    for pancake in pancakes:
        r, h = pancake
        to_append = {}
        for size in candidates_per_size:
            candidates = candidates_per_size[size]
            try:
                best_candidate = max(candidates, key=lambda c: syrup(c + [pancake]))
            except ValueError:
                break
            new_candidate = best_candidate + [pancake]
            if size == k - 1:
                best = max(best, syrup(new_candidate))
            else:
                to_append[size] = new_candidate.copy()

        for size in to_append:
            candidates_per_size[size + 1].append(to_append[size])

    print(best)

if __name__ == '__main__':
    solve()
