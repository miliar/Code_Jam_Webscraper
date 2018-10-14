#!/usr/bin/env python
"""
Module docstring
This serves as a long usage message.
"""
import sys

T = int(sys.stdin.readline())

for j in range(1, T+1):
    N = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip().split(" ")
    numbers = []
    for number in a:
        numbers.append(int(number))
    deranged_nums = 0
    for i in range(len(numbers)):
        if numbers[i] != i + 1:
            deranged_nums += 1
    print "Case #%d: %d" % (j, deranged_nums)
