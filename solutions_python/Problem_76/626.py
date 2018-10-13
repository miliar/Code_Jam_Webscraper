#!/usr/bin/python

"""
Candy Splitting problem solution
(GCJ 2011, Qualification Round)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: candy_splitting.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    C = int(in_file.readline())
    values = map(int, in_file.readline().split(" "))
    values.sort()
    # check possibility
    txor = values[0]
    total = 0
    for i in values[1:]:
        txor ^= i
        total += i
    if txor > 0:
        total = "NO"
    print "Case #%d: %s" % (cur_case + 1, total)

# close input file
in_file.close()

    
        
