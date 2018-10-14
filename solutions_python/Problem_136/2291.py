#!/usr/bin/env python

import sys

count = 0
case = 1
for line in sys.stdin:
    if count:
        values = line.split()
        c = float(values[0])
        f = float(values[1])
        x = float(values[2])
        speed = 2.0
        time = 0.0
        while x / (speed + f) + c / speed < x / speed:
            time += c / speed
            speed += f
        time += x / speed
        print("Case #" + str(case) + ": " + str(time))
        case += 1
    count += 1
