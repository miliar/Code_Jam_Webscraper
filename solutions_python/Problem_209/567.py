from typing import List

from math import pi

import itertools

class Pancake:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface(self):
        return pi * self.radius ** 2

    def rim(self):
        return 2 * pi * self.radius * self.height

    def __repr__(self):
        return '{{r = {}, h = {}}}'.format(self.radius, self.height)


def find_best_stack_area(pancakes: List[Pancake], k: int) -> float:
    maxarea = 0
    beststack = None
    for p in [p for p in itertools.permutations(pancakes, k) if sorted(p, key=lambda item:item.radius, reverse=True) == list(p)]:
        a = area(p)
        if a > maxarea:
            maxarea = a
            beststack = p

    return maxarea, beststack


def find_best_stack_area_fast(pancakes: List[Pancake], k: int) -> float:
    sorted_radius = sorted(pancakes, key=lambda item:item.radius, reverse=True)
    sorted_rim = sorted(pancakes, key=lambda item:item.rim(), reverse=True)

    possible_bottom_pancakes = sorted_radius[0:len(pancakes) - k + 1]

    best_stack = None
    best_area = 0
    for bottom in possible_bottom_pancakes:
        remaining_pancakes = [p for p in sorted_rim if p.radius <= bottom.radius and p != bottom]
        stack = [bottom] + sorted(remaining_pancakes[0:k-1], key=lambda item:item.rim(), reverse=True)

        a = area(stack)
        if a > best_area:
            best_stack = stack
            best_area = a

    return area(best_stack), best_stack


def area(stack: List[Pancake]) -> float:
    return stack[0].surface() + sum([pc.rim() for pc in stack])


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    pancakes = []
    for j in range(n):
        r, h = [int(s) for s in input().split(" ")]
        pancakes.append(Pancake(r, h))

    a, s = find_best_stack_area_fast(pancakes, k)
    # a2, s2 = find_best_stack_area(pancakes, k)
    # if a != a2:
    #     raise ValueError('{} != {}\n{}\n{}'.format(a, a2, s, s2))

    print("Case #{}: {}".format(i, a))