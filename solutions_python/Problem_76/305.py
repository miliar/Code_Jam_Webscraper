#!/usr/bin/env python

import itertools
import array
import math
import sys
import fractions
import copy

# Print the result
def print_result(res):
    if res == -1:
        return  "NO"
    else:
        return str(res)

# Check if the problem has no solution
def has_solution(l):
    res = 0
    for e in l:
        res ^= e
    return res == 0

# List sum using xor
# def list_xor(l):
#     res = 0
#     for e in l:
#         res ^= e
#     return res

# Compute result
def result(l):
    if not has_solution(l):
        sys.stderr.write("Fast NO\n")
        return -1

    l.sort()
    return sum(l[1:])

# Nb tests
T = int(raw_input())
sys.stderr.write(str(T) + " test to compute\n")

# Process tests
for x in xrange(1, T + 1):
    sys.stderr.write("Load input of test " + str(x) +  "...\n")

    N = int(raw_input())
    l = raw_input().split(" ")
    l2 = [(int(e)) for (e) in l]

    y = result(l2)
    print "Case #" + str(x) + ": " + print_result(y)
    sys.stderr.write("\n")
