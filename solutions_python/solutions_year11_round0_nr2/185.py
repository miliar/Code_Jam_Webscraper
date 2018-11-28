#!/usr/bin/python

import sys
import re

lines = []
with open(sys.argv[1], 'r') as FILE:
    lines = FILE.readlines()

cases = []
for line in lines[1:]:
    line = line.split()
    C = int(line[0])
    D = int(line[C + 1])
    cases.append((line[1:C + 1], line[C + 2:C + 2 + D], line[-1]))

casenumber = 0
for case in cases:
    casenumber += 1
    res = ''

    combs = {}
    for c in case[0]:
        combs[c[:2]] = c[-1]
        combs[c[:2][::-1]] = c[-1]

    ops = []
    for o in case[1]:
        for i in range(2): ops.append(re.compile(o[i] + '.*' + o[1 - i]))

    for elem in case[2]:
        res += elem

        while (len(res) > 1) and (res[-2:] in combs):
            res = res[:-2] + combs[res[-2:]]

        if len(res) > 1:
            for op in ops:
                if op.search(res):
                    res = ''
                    break

    res = str(list(res)).replace("'", '')
    print("Case #{0}: {1}".format(casenumber, res))
