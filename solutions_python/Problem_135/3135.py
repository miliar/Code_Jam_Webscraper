#!/usr/bin/env python

from sys import stdin

cases = int(stdin.readline())

for i in range(1, cases + 1):
    row = int(stdin.readline())

    for k in range(1, 5):
        line = stdin.readline()
        if k == row:
            nums = set(line.split())

    row = int(stdin.readline())
    for k in range(1, 5):
        line = stdin.readline()
        if k == row:
            nums2 = set(line.split())

    same = nums.intersection(nums2)
    if len(same) == 1:
        (element,) = same
        print("Case #" + str(i) + ": " + str(element))
    elif len(same) > 1:
        print("Case #" + str(i) + ": Bad magician!")
    else:
        print("Case #" + str(i) + ": Volunteer cheated!")
