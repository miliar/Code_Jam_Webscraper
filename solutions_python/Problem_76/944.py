#!/usr/pubsw/bin/python
import sys

def processExample(example_str, case_num):
    vals = [int(n) for n in example_str.split(' ')]

    runningAmmt = 0
    for n in vals:
        runningAmmt ^= n

    if runningAmmt != 0:
       print("Case #" + str(case_num) + ": NO")
    else:
       maxVal = sum(vals) - min(vals)
       print("Case #" + str(case_num) + ": " + str(maxVal))

f = open(sys.argv[1])
lineNum = 1
for line in f:
    if (lineNum % 2) == 1 and lineNum > 1:
       processExample(line, (lineNum-1)/2)
    lineNum += 1
