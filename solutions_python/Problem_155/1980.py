#!/usr/bin/python

import sys

if len(sys.argv) == 1:
    print("Error: No Input file Provided")
    sys.exit(1)

fname = sys.argv[1]

lines = open(fname).readlines()
out = open(fname + ".out", "w")

lines.pop(0)

lines = [line.strip() for line in lines]

c = 1


for row in lines:
    req = row.split()[1]
    added = 0
    count = 0
    for i in range(len(req)):
        if int(req[i]) != 0:
            if i > count:
                added += i - count
                count += i - count
            count += int(req[i])
    out.write("Case #%s: %s\n" % (c, added))
    c += 1

out.close()