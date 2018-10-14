#!/usr/bin/python3
# Python version >= 3.6
# codejam 2017 1C  
# 2017-04-30  05:00  (GMT-4)

from math import pi
from heapq import nlargest
from bisect import bisect

# since N<=1000
# idc about checking each base pancake. It'll be O(N^2)
# sure not optimal, but will work


def check_with_base_radius(side_areas, radii, base_radius, k):
    where = bisect(radii, (base_radius)) - 1
    if where < k-1:
        return 0
    last = side_areas[where]
    topk = nlargest(k-1, side_areas[:where])
    return base_radius**2 + last + sum(topk)

def check_all(side_areas, radii, k):
    return max(check_with_base_radius(side_areas, radii, b, k) for b in set(radii))



def consume_input(N):
    pancakes = []
    for _ in range(N):
        pancakes.append(tuple(int(x) for x in input().split()))
    pancakes.sort()
    radii = [x[0] for x in pancakes]
    side_areas = [2 * x[0] * x[1] for x in pancakes]
    return side_areas, radii
    


if __name__=="__main__":
    T = int(input())

    for case in range(T):
        print(f"Case #{case+1}: ", end="")
        N, K = (int(x) for x in input().split())
        side_areas, radii = consume_input(N)
        print(pi * check_all(side_areas, radii, K))

        

