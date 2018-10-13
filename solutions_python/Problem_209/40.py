from math import ceil, floor, pi
import numpy as np
from functools import lru_cache


def area_top(r):
    return r**2 * pi

def area_side(r, h):
    return 2*r*h*pi

# @lru_cache(maxsize=None)
def stack_pancakes(N, K, radii, heights):
    side_areas = np.array([area_side(r, h) for r, h in zip(radii, heights)])

    area_opt = 0
    for i_0 in range(N):
        area_curr = area_top(radii[i_0]) + side_areas[i_0]

        if K > 1:
            sides = 1*side_areas
            sides[i_0] = 0

            top_sides = np.sort(sides)[-K+1:]
            area_curr += top_sides.sum()

        area_opt = max((area_curr, area_opt))

    return area_opt


if __name__=='__main__':
    PATH_IN = 'A-large.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline().split()
        N = int(line[0])
        K = int(line[1])
        print(N, K)

        radii = np.zeros(N)
        heights = np.zeros(N)

        for i in range(N):
            line = f_in.readline().split()
            radii[i] = int(line[0])
            heights[i] = int(line[1])

        res = '%.9f' % stack_pancakes(N, K, radii, heights)

        print('Case #%i: %s' % (t+1, res))
        print()
        f_out.write('Case #%i: %s\n' % (t+1, res))
