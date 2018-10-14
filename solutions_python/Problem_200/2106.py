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

def su(number):
    for i in range(1,len(number)):
        if number[i] < number[i-1]:
            return number[:i], number[i:]
    return number,[]

def solve(number):
    s,u = su(number)
    while u != []:
        u = [9] * len(u)
        s[-1] = s[-1] - 1
        s, u = su(s+u)
    return s

for i in range(T):
    case = f.readline().strip()
    number = map(int, case)

    out_case = solve(number)
    out_case = int("".join(map(str,out_case)))

    print "Case #" + str(i + 1) + ": " + str(out_case)
    fo.write("Case #" + str(i + 1) + ": " + str(out_case) + '\n')
