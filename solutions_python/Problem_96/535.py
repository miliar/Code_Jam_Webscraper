#!/usr/bin/python

"""
Dancing With the Googlers problem solution
(GCJ 2012, Qualification Round)
Author: a5kin
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: dancing_with_the_googlers.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    tmp_list = map(int, in_file.readline().split(" "))
    N, S, p = tmp_list[0], tmp_list[1], tmp_list[2]
    points = tmp_list[3:]
    max_best = 0
    # processing triplets
    surprising_candidates = 0
    for score in points:
        best = int(math.ceil(score / 3.))
        if best >= p:
            max_best += 1
        if best == (p - 1) and score > 1 and score % 3 != 1:
            surprising_candidates += 1
    max_best += min(surprising_candidates, S)
    # output results
    print "Case #%d: %s" % (cur_case + 1, max_best)

# close input file
in_file.close()

    
        
