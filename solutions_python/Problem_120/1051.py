from __future__ import division
# Google Code Jam (2013): Qualification Round

# Code Jam Utils
# Can be found on Github's Gist at:
# https://gist.github.com/Zren/5376385
from codejamutils import *

problem_id = 'A'

#problem_size = 'sample'
#problem_size = 'small'
problem_size = 'large'

opt_args = {
    #'practice': True,
    'log_level': DEBUG,
    'filename': 'A-small-attempt0',
}


import math
area_map = {}

# line_paint = (math.pi * b_r * b_r - math.pi * a_r * a_r) / math.pi
# (b - a)^2
# math.pi is canceled out

def area(r):
    area = math.pi * r * r
    return area
    """
    if r in area_map:
        return area_map[r]
    else:
        area = math.pi * r * r
        area_map[r] = area
        return area
    """

def num_rings(start_r, paint_milli):
    r = start_r
    black_rings = 0

    #"""
    x = start_r * 2 + 1
    while True:
        paint_used = x
        if paint_milli >= paint_used:
            # paint
            paint_milli -= paint_used
            black_rings += 1
            x += 4
        else:
            return black_rings
    #"""

    #"""
    while True:

        a_r = r * r
        b_r = (r+1) * (r+1)
        #info('a_r', a_r)
        #info('b_r', b_r)
        line_area = b_r - a_r
        #info('line_area',line_area)
        paint_used = line_area
        info('paint_used', paint_used)
        if paint_milli >= paint_used:
            # paint
            paint_milli -= paint_used
            black_rings += 1
            r += 2
        else:
            return black_rings
    #"""

with Problem(problem_id, problem_size, **opt_args) as p:
    for case in p:
        info('Case', case.case)
        start_r, paint_milli = case.readints()
        info('r', start_r)
        info('t', paint_milli)
        case.writecase(num_rings(start_r, paint_milli))
