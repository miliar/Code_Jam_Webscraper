#! /usr/bin/python
import sys
import math

line = sys.stdin.readline()
line = line.rstrip()
case = int(line)

for test in range(case):
    line = sys.stdin.readline()
    line = line.rstrip()
    strs = line.split()
    numbers = [int(item) for item in strs]
    
    N = numbers[0]
    S = numbers[1]
    p = numbers[2]
    numbers = numbers[3:]
    count = 0
    for item in numbers:
        if item >= (p - 1) * 3 + 1:
            count += 1
        elif item >= (p - 2) * 2 + p and p >= 2:
            if S > 0:
                S -= 1
                count += 1

    print "Case #%d: %d" % (test + 1, count)
    
