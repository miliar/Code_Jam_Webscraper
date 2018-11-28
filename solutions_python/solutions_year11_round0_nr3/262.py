#!/usr/bin/env python
"""
Module docstring
This serves as a long usage message.
"""
import sys

T = int(sys.stdin.readline())
for j in range(T):
    N = int(sys.stdin.readline())
    candies_s = sys.stdin.readline().rstrip().split(" ")
    C = []
    for candy in candies_s:
        C.append(int(candy))

    found_an_odd_one = False
    for i in range(22):
        mask = 2 ** i
        sum_of_bits_in_this_place = 0
        for ci in C:
            if ci & mask > 0:
                sum_of_bits_in_this_place += 1
        if sum_of_bits_in_this_place % 2 != 0: #odd
            found_an_odd_one = True
            break
    if found_an_odd_one:
        print "Case #%d: NO" % (j + 1)
        continue
    C.sort()
    C.pop(0)
    sum = 0
    for ci in C:
        sum += ci
    print "Case #%d: " % (j + 1), sum
