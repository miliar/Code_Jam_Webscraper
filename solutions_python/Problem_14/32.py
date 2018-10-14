#!/usr/bin/python

"""
Triangle Areas problem solution
(GCJ 2008, Round 2)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: triangle_areas.py <input file>"
    sys.exit(0)

# get number of cases
num_cases = int(in_file.readline())

# begin prosessing cases
for cur_case in range(num_cases):

    # get init data
    values = in_file.readline().split(" ")
    n = int(values[0])
    m = int(values[1])
    a = int(values[2])

    if n * m < a:
        print "Case #%d: IMPOSSIBLE" % (cur_case + 1,)
        continue
    else:
        breakfl = False
        for i in range(n + 1):
            if breakfl:
                break
            for j in range(m + 1):
                if breakfl:
                    break
                for k in range(n + 1):
                    if breakfl:
                        break
                    for l in range(m + 1):
                        s = i * l - j * k
                        if a == s or a == -s:
                            print "Case #%d: 0 0 %d %d %d %d" % (cur_case + 1, i, j, k, l)
                            breakfl = True
                            break

in_file.close()

