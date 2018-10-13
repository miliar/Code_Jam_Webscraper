#! /usr/bin/env python
#
#   C. Theme Park
#

from __future__ import print_function
from sys import stdin

N = int(stdin.readline())
for case in range(1, N+1):
    runs, seats, num_groups = map(int, stdin.readline().split())
    groups = list(map(int, stdin.readline().split()))
    income = 0
    head = 0
    for r in range(runs):
        seats_left = seats
        for g in range(num_groups):
            gsize = groups[(head+g) % num_groups]
            if seats_left < gsize:
                g -= 1
                break
            income += gsize
            seats_left -= gsize
        head = (head+g+1) % num_groups
    print("Case #{0}:".format(case), income)
