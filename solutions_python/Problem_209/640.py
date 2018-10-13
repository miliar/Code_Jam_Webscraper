#!/usr/bin/env python3

"""
Needs K pancakes
Has N pancakes.
N ≥ K

Choose K, sort them by radii
"""

import sys
import math
from collections import namedtuple
import itertools


def surface_of_a_sorted_stack(pancakes_stack):
    """Biggest at the end.
    """
    sides = 0
    for pancake in pancakes_stack:
        sides += pancake.side_surface()
    return sides + pancakes_stack[-1].top_surface()


Pancake = namedtuple('Pancake', 'radius, height')
class Pancake:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def side_surface(self):
        return self.height * self.radius * 2 * math.pi

    def top_surface(self):
        return self.radius ** 2 * math.pi

    def __repr__(self):
        return 'Pancake(h={}, r={}, side_surface={}, top_surface={}'.format(
            self.height,
            self.radius,
            self.side_surface(),
            self.top_surface())


def solve(qty_needed, stock):
    # print("Pick {} pancakes".format(qty_needed), "in:\n -", "\n - ".join(repr(p) for p in stock))
    best = 0
    for comb in itertools.combinations(sorted(stock, key=lambda p: p.radius), qty_needed):
        surface = surface_of_a_sorted_stack(list(comb))
        best = best if best > surface else surface
    return best


def main():
    with open(sys.argv[1]) as ifile:
        qty_test_cases = int(ifile.readline())
        for test_case in range(qty_test_cases):
            qty_in_stock, qty_needed = map(int, ifile.readline().split())
            stock = []
            for _ in range(qty_in_stock):
                stock.append(Pancake(*map(int, ifile.readline().split())))
            print("Case #{}: {}".format(test_case + 1, solve(qty_needed, stock)))

main()
