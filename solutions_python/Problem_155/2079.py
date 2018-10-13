#!/usr/bin/env python3

import sys

lines = "".join(sys.stdin).split("\n")[1:]
lines = [x for x in lines if x != ""]


def calc(nums):
    numlist = list(nums)
    count = 0
    need = 0
    for idx, val in enumerate(numlist):
        count += int(val)
        if count < idx + 1:
            need += (idx + 1) - count
            count += (idx + 1) - count
    return need


for idx, line in enumerate(lines):
    max_level, val = line.split(" ")
    audience_need = calc(val)

    print("Case #%d: %d" % (idx + 1, audience_need))
