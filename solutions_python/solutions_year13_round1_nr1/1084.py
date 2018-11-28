from math import sqrt, floor
from sys import *

__author__ = 'joranvar'


def circles(r, t):
    radius = r + 1
    rings = 0
    while t > 0:
        t -= 2 * radius - 1
        if t >= 0:
            rings += 1
        radius += 2
    return rings


def circles2(r, t):
    # Each circle gains 4 ml
    # Root circle = 2r - 1 ml
    # Area under graph = (2r - 1) * x + (0.5 * x * 4x)
    # Where x is the number of circles drawn
    # Using the root formula:
    x = ((-2 * r) + 1 + sqrt((2 * r - 1) ** 2 - (8 * -t))) / 4
    # But a whole circle needs to be painted
    # We ran out of paint
    return floor(x)

#stdin = open("A.in")
T = int(stdin.readline().strip())
#stdout = open("A.out", "w")
for case_no in range(T):
    rings = circles2(*map(int, stdin.readline().split()))
    stdout.write("Case #{0}: {1}\n".format(case_no + 1, rings))

