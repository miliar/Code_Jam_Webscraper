#! /usr/bin/python

import sys


if len(sys.argv) < 2:
    print("Usage: ./p1.py <input file>")
    sys.exit(1)

try:
    fin = open(sys.argv[1])
except IOError:
    print("Input file not found")
    sys.exit(1)

data = fin.readlines()
fin.close()
ind = 1
num = int(data[0].strip())

for i in xrange(num):
    row = data[ind].strip().split()
    ind += 1
    c = float(row[0])
    f = float(row[1])
    goal = float(row[2])

    cookies = 0
    time = 0
    rate = 2
    while cookies < goal:
        t1 = (goal - cookies) / rate
        t2 = (c - cookies) / rate + goal / (rate + f)
        if t1 < t2:
            time += t1
            cookies = goal
        else:
            time += (c - cookies) / rate
            rate += f
            cookies = 0
    print "Case #%d: %.7f"%(i+1, time)

sys.exit(0)
