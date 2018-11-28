#!/usr/bin/env python3

from math import pi


def calc_surface(pancakes):
    circle = pancakes[-1][0]**2
    cylinder = 2 * sum(pancake[0] * pancake[1] for pancake in pancakes)
    return pi * (circle + cylinder)


def max_syrup(k, pancakes):
    surfaces = []
    while len(pancakes) >= k:
        pancakes.sort()
        bottom = pancakes.pop()
        pancakes.sort(key=lambda x: x[0]*x[1], reverse=True)
        selected = pancakes[:k-1] + [bottom]
        surfaces += [calc_surface(selected)]
    return max(surfaces)


def main():
    for case in range(int(input())):
        n, k = [int(n) for n in input().split()]
        pancakes = [[int(n) for n in input().split()] for _ in range(n)]
        answer = max_syrup(k, pancakes)
        print('Case #{}: {}'.format(case+1, answer))


if __name__ == '__main__':
    main()
