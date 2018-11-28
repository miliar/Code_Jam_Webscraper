#!/usr/bin/python3
import sys
from decimal import Decimal


inp = open(sys.argv[1], 'r')
out = open('outb.txt', 'w')
cases = inp.readline()
for i in range(int(cases)):
    c, f, x = [Decimal(x) for x in inp.readline().split()]
    p = 2  # production rate
    time = 0
    while(True):
        without_farm = x / p
        with_farm = c / p + x / (p + f)
        if without_farm < with_farm:
            time += x / p
            break
        else:
            time += c / p
            p += f
    out.write("Case #" + str(i + 1) + ": " + str(time) + '\n')
