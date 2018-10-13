#!/usr/bin/python

"""
Magicka problem solution
(GCJ 2011, Qualification Round)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: magicka.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    test_line = in_file.readline().split(" ")
    C = int(test_line[0])
    combine = {}
    for pair in test_line[1:C+1]:
        combine[pair[:2]] = pair[2]
        combine[pair[1]+pair[0]] = pair[2]
    D = int(test_line[C+1])
    opposite = {}
    for pair in test_line[C+2:C+D+2]:
        opposite[pair[0]] = pair[1]
        opposite[pair[1]] = pair[0]
    N = int(test_line[-2])
    cast_order = test_line[-1]
    # begin modelling
    cast_model = ""
    base_used = {"Q": 0, "W": 0, "E": 0, "R": 0, "A": 0, "S": 0, "D": 0, "F": 0, }
    for element in cast_order:
        if base_used.has_key(element):
            base_used[element] += 1
        cast_model += element
        if combine.has_key(cast_model[-2:]):
            base_used[cast_model[-2]] -= 1
            base_used[cast_model[-1]] -= 1
            cast_model = cast_model[:-2] + combine[cast_model[-2:]]
        if opposite.has_key(cast_model[-1]) and base_used[opposite[cast_model[-1]]] > 0:
            cast_model = ""
            base_used = {"Q": 0, "W": 0, "E": 0, "R": 0, "A": 0, "S": 0, "D": 0, "F": 0, }
    print "Case #%d: %s" % (cur_case + 1, "[%s]" % ', '.join(list(cast_model)[:-1]))

# close input file
in_file.close()

    
        
