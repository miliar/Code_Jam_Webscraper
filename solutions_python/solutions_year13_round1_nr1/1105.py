import math

import codejam

problems = (map(int, line.split()) for line in codejam.read())

def area(radius):
    return math.pi * (radius ** 2)


def size_needed(current_radius):
    return area(current_radius) - area(current_radius - 1)


def s(r):
    return 2 * r + 1

def solve(r, t):
    current_radius = r

    n = 0
    paint_left = t
    current_size = s(r)
    while paint_left >= current_size:
        n += 1
        paint_left -= current_size
        current_radius += 2
        current_size = s(current_radius)

    return n


for i, problem in enumerate(problems):
    print 'Case #{0}: {1}'.format(i+1, solve(problem[0], problem[1]))
