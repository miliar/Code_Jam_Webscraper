#!/usr/bin/python

"""
Load Testing problem solution
(GCJ 2010, Round 1B)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: load_testing.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    L, P, C = map(int, in_file.readline().split(" "))
    points = 0
    while L * C < P:
        points += 1
        P = math.ceil(float(P) / C)
    tests = 0
    while points > 0:
        points = math.floor(points / 2)
        tests += 1
    # output result
    print "Case #%d: %d" % (cur_case + 1, tests)

# close input file
in_file.close()

    
        
