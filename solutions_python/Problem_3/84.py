#!/usr/bin/env python

import random
from math import sqrt, floor, ceil, pi, asin

debug = True

def read_data():
    n = int(raw_input())
    cases = []
    for i in range(n):
        case = {}
        case["f"], case["rr"], case["t"], case["r"], case["g"] = map(float, raw_input().split())
        cases.append(case)

    return cases

def process(f, rr, t, r, g):
    def hole_coords(i, j):
        x0 = r + i*(2*r+g) + f
        x1 = x0 + g - 2*f
        y0 = r + j*(2*r+g) + f
        y1 = y0 + g - 2*f
        return x0, x1, y0, y1

    def is_hole_inside(i, j, hr):
        x0, x1, y0, y1 = hole_coords(i, j)
        max_r = max(x0**2 + y0**2, x1**2 + y0**2, x0**2 + y1**2, x1**2 + y1**2)
        return max_r < hr**2

    def is_hole_outside(i, j, hr):
        x0, x1, y0, y1 = hole_coords(i, j)
        min_r = min(x0**2 + y0**2, x1**2 + y0**2, x0**2 + y1**2, x1**2 + y1**2)
        return min_r > hr**2

    def cut_area(i, j, hr):
        def integral(x, r):
            return r**2/2 * asin(x/r) + x*sqrt(r**2 - x**2)/2

        x0, x1, y0, y1 = hole_coords(i, j)
        if sqrt(hr**2 - x0**2) < y1:
            start = x0
        else:
            start = sqrt(hr**2 - y1**2)
        if sqrt(hr**2 - x1**2) > y0:
            end = x1
        else:
            end = sqrt(hr**2 - y0**2)

        area = integral(end, hr) - integral(start, hr)
        area += (start-x0)*y1
        area -= (end-x0)*y0
        return area

    er = rr-t-f
    h = int(ceil(er/(2*r+g)))

    hole_area = 0.0
    for i in range(0, h):
        for j in range(0, h):
            if is_hole_outside(i, j, er):
                continue
            elif is_hole_inside(i, j, er):
                hole_area += (g-2*f)**2
            else:
                hole_area += cut_area(i, j, er)

    # Symmetry of holes
    hole_area *= 4

    total_area = pi*rr**2
    interior_area = pi*er**2
    hit_area = interior_area - hole_area
    ring_area = total_area - interior_area
    return (ring_area + hit_area) / total_area

for i, case in enumerate(read_data()):
    print "Case #%d: %f" % (i+1, process(**case))
