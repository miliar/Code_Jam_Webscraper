#!/usr/bin/env python3
from os.path import basename
from math import pi

# Any imports included here are either pip installable or included with
# anaconda which is available from https://www.continuum.io/downloads


def get_stack(radius_bottom, height_bottom, pancakes, order_height):
    pancakes = sorted(pancakes, key=lambda x: 2*pi*x[0]*x[1], reverse=True)
    # assert 2*pi*pancakes[0][0]*pancakes[0][1] >= 2*pi*pancakes[-1][0]*pancakes[-1][1]
    area = radius_bottom*radius_bottom*pi + 2*pi*radius_bottom*height_bottom
    for i in range(order_height-1):
        r, h = pancakes[i]
        area += 2*pi*r*h
    return area


filename = 'inputs/A-large.in'

with open(f'{filename.split(".")[0]}.in', 'rt') as f:
    input_lines = [l.strip() for l in f.readlines()]

# assert int(input_lines[0])+1 == len(input_lines)
input_lines = input_lines[1:]

solutions = []
i = 0
case_number = 1
while i < len(input_lines):
    n_available, order_height = map(int, input_lines[i].split())
    i += 1
    pancakes = []
    for n in range(n_available):
        radius, height = map(int, input_lines[i].split())
        i += 1
        pancakes.append((radius, height))

    areas = [
        get_stack(radius, height, pancakes[:n] + pancakes[n+1:], order_height)
        for n, (radius, height) in enumerate(pancakes)
    ]
    solution = max(areas)
    solutions.append(f'Case #{case_number}: {solution}')
    case_number += 1

print(*solutions, sep='\n')
with open(f'outputs/{basename(filename).split(".")[0]}.out', 'wt') as f:
    f.write('\n'.join(solutions))
