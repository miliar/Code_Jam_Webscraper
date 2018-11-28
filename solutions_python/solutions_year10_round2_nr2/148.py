#!/usr/bin/python

"""
Picking Up Chicks problem solution
(GCJ 2010, Round 1B)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: picking_up_chicks.py <input file>"
    sys.exit(0)

# get number of cases
C = int(in_file.readline())

# begin prosessing cases
for cur_case in range(C):
    # get constants
    N, K, B, T = map(int, in_file.readline().split(" "))
    # get coordinates
    Xi = map(int, in_file.readline().split(" "))
    # get velocities
    Vi = map(int, in_file.readline().split(" "))
    chicks = zip(Xi, Vi)
    chicks.sort()
    chicks.reverse()
    # calculate swaps
    total_swaps = 0
    swaps = 0
    chicks_count = 0
    answer = "IMPOSSIBLE"
    for Xi, Vi in chicks:
        if float(B - Xi) / float(Vi) > T:
            swaps += 1
        else:
            chicks_count += 1
            total_swaps += swaps
        if chicks_count >= K:
            answer = str(total_swaps)
            break
    # output result
    print "Case #%d: %s" % (cur_case + 1, answer)

# close input file
in_file.close()

    
        
