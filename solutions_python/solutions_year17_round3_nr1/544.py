# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import math

def get_surface(p):
    return math.pi * p[0]**2

def get_side_surface(p):
    return 2 * math.pi * p[0] * p[1]

def get_area(p):
    if p is None:
        return 0
    return get_surface(p) + get_side_surface(p)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    str_number = input().split(" ")
    n, k = int(str_number[0]), int(str_number[1])
    pancakes = []
    for j in range(n):
        str_number = input().split(" ")
        pancakes.append((int(str_number[0]), int(str_number[1])))
    pancakes_hsorted = sorted(pancakes, key=lambda x: get_side_surface(x),reverse=True)
    sol = sorted(pancakes_hsorted[:(k-1)], reverse=True)
    for p in sol:
        pancakes.remove(p)
    additional_area = 0
    if len(sol) > 0:
        for p in pancakes:
            if p[0] > sol[0][0]:
                additional_area = max(additional_area, get_side_surface(p) + (get_surface(p) - get_surface(sol[0])))
            else:
                additional_area = max(additional_area, get_side_surface(p))
    else:
        sol = [sorted(pancakes, key=lambda x: get_area(x), reverse=True)[0]]
    area = additional_area
    for j in range(len(sol)):
        area += get_area(sol[j])
        if j+1 < len(sol):
            area -= get_surface(sol[j+1])
    print("Case #{}: {:.9f}".format(i, area))
