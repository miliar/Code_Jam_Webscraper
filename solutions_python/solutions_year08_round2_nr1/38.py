#!/usr/bin/python

"""
Crop Triangles problem solution
(GCJ 2008, Round 1B)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: crop_triangles.py <input file>"
    sys.exit(0)

# get number of cases
num_cases = int(in_file.readline())

# begin prosessing cases
for cur_case in range(num_cases):

    # get init values
    values = in_file.readline().split(" ")
    n = int(values[0])
    a = int(values[1])
    b = int(values[2])
    c = int(values[3])
    d = int(values[4])
    x0 = int(values[5])
    y0 = int(values[6])
    m = int(values[7])

    # generate vertexes
    vertexes = []
    x = x0
    y = y0
    vertexes.append((x, y))
    for i in range (1, n):
        x = (a * x + b) % m
        y = (c * y + d) % m
        vertexes.append((x, y))

    # looping vertexes
    num_triangles = 0;
    for i in range(len(vertexes)):
        for j in range(len(vertexes)):
            if i != j:
                for k in range(len(vertexes)):
                    if k != i and k != j:
                        x1, y1 = vertexes[i]
                        x2, y2 = vertexes[j]
                        x3, y3 = vertexes[k]
                        if (x1 + x2 + x3) % 3 == 0 and (y1 + y2 + y3) % 3 == 0:
                            num_triangles += 1
    print "Case #%d: %d" % (cur_case + 1, int(num_triangles / 6))
                        
