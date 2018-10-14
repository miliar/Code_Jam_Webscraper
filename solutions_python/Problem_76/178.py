#!/usr/bin/python

def paul_add(*nums):
    retv = 0
    for num in nums:
        retv = (retv & num) ^ (retv | num)

    return retv

import sys

lines = []
with open(sys.argv[1], 'r') as FILE:
    lines = FILE.readlines()[1:]

cases = []
for line in lines[1::2]:
    cases.append(list(map(int, line.split())))

casenumber = 0
for case in cases:
    casenumber += 1

    sean = sorted(case)
    paul = [sean[0]]
    sean = sean[1:]
    piles = (paul_add(*sean), paul_add(*paul))
    while (piles[0] != piles[1]):
        paul.append(sean[0])
        if len(sean) > 1:
            del(sean[0])
        else:
            break
        piles = (paul_add(*sean), paul_add(*paul))

    retval = "NO"
    if piles[0] == piles[1]:
        retval = max(sum(sean), sum(paul))

    print("Case #{0}: {1}".format(casenumber, retval))
