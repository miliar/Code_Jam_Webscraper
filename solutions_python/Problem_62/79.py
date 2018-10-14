#!/usr/bin/python

"""
Rope Internet problem solution
(GCJ 2010, Round 1B)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: rope_internet.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get number of points
    N = int(in_file.readline())
    # simulate wiring
    intersects = 0
    buildings = []
    for i in range(N):
    # get coordinates
        x, y = map(int, in_file.readline().split(" "))
        def is_intersect(coords):
            global x, y
            left, right = coords
            return x>left and y<right or x<left and y>right 
        intersects += len(filter(is_intersect, buildings))
        buildings.append((x,y))
    # output result
    print "Case #%d: %s" % (cur_case + 1, intersects)

# close input file
in_file.close()

    
        
