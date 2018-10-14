import sys
from math import pi
from functools import partial


def noop(*args, **kwargs):
    pass


# log = partial(print, file=sys.stderr)
log = noop


def top(pancake):
    r, h = pancake
    return pi * r ** 2


def side(pancake):
    r, h = pancake
    return 2 * pi * r * h


def solve(n, k, pancakes):
    pancakes.sort(key=top, reverse=True)  # sort by radius, biggest first
    best = 0
    for x, pancake in enumerate(pancakes):  # pick the bottom pancake
        log(x, pancake)

        others = pancakes[x + 1:]
        others.sort(key=side, reverse=True)
        log(others)
        # from the others, pick the ones with the largest sides
        a = top(pancake) + side(pancake) + sum(map(side, others[:k - 1]))
        if a > best:
            best = a
    return best


def main():
    t = int(input())
    for case in range(1, 1 + t):
        n, k = map(int, input().split())
        pancakes = [tuple(map(int, input().split())) for _ in range(n)]
        answer = solve(n, k, pancakes)
        print(f"Case #{case}: {answer}")


main()
