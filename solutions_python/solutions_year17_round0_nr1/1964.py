#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    input_file = sys.argv[1]
except:
    input_file = sys.argv[0].split(".")[0] +  ".in"

output_file = input_file.split(".")[0] + ".out"

f = open(input_file, 'r')
fo = open(output_file, 'w')

T = int(f.readline())

def solve(pancakes, flipper):
    c = 0
    for i in range(len(pancakes) - flipper + 1):
        if not pancakes[i]:
            for j in range(flipper):
                pancakes[i + j] = not pancakes[i + j]
            c += 1
    if all(pancakes):
        return c
    else:
        return "IMPOSSIBLE"

for i in range(T): # [0,1,2,...,T-1]
    case = f.readline().strip()
    pancakes, flipper = case.split(" ")

    flipper = int(flipper)
    pancakes = map(lambda p: True if p == '+' else False, pancakes)

    out_case = solve(pancakes, flipper)

    print "Case #" + str(i + 1) + ": " + str(out_case)
    fo.write("Case #" + str(i + 1) + ": " + str(out_case) + '\n')
