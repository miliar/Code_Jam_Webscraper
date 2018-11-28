# -*- coding: utf-8 -*-
import sys
import math


def solve(total, k, pancakes):
    print()
    # contain radius, side area (no pi)
    scored_pancakes = []
    for pancake in pancakes:
        scored_pancakes.append((pancake[0], 2*pancake[0]*pancake[1]))
    # sort by score
    sorted_scored_pancakes = sorted(scored_pancakes, key=lambda x: x[1])
    sorted_scored_pancakes.reverse()
    print (sorted_scored_pancakes)
    max_area = -1
    for i in range(total):
        any_pc = sorted_scored_pancakes[i]
        if i != total-1:
            cp_list = [any_pc] + sorted_scored_pancakes[:i] + sorted_scored_pancakes[i+1:]
        else:
            cp_list = [any_pc] + sorted_scored_pancakes[:-1]
        max_radius = 0
        area=0
        for pc in cp_list[:k]:
            area += pc[1]
            max_radius = max(max_radius, pc[0])
        area += max_radius**2
        if area > max_area:
            print(max_radius)
            max_area = area
    return max_area * math.pi


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f_in, \
             open(sys.argv[1] + ".out", "w") as f_out:
        count = int(f_in.readline())
        for i in range(count):
            total, k = f_in.readline().strip().split()
            total, k = int(total), int(k)
            pancakes = []
            for j in range(total):
                radius, height = f_in.readline().strip().split()
                radius, height = int(radius), int(height)
                pancakes.append((radius, height))
            solution = solve(total, k, pancakes)
            f_out.write("Case #%i: %.8f\n" % (i+1, solution))
