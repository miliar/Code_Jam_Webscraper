from __future__ import division

from sys import stdin, stdout
from basics import *
import math
import pdb

def solve(pancakes, N, K):
    max_area = 0
    pancakes.sort(key=lambda p:p[0], reverse=True)
    side_areas = [2 * math.pi * p[0] * p[1] for p in pancakes]

    for top_i in range(N - K + 1):
        top = pancakes[top_i]
        
        area = math.pi * top[0] ** 2
        area += side_areas[top_i]
        area += sum(sorted(side_areas[(top_i+1):], reverse=True)[:(K-1)])

        max_area = max(max_area, area)

    return max_area

T = read_val()

for t in range(T):
    N, K = read_vals()
    pancakes = read_lines(N)

    result = solve(pancakes, N, K)

    stdout.write("Case #{}: {}\n".format(t+1, result))