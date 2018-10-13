#!/usr/bin/python

"""
Perfect Harmony problem solution
(GCJ 2011, Round 1B)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: perfect_harmony.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    N, L, H = map(int, in_file.readline().split(" "))
    notes = map(int, in_file.readline().split(" "))
    # begin calculation
    for test_note in range(L, H + 1):
        final_note = test_note
        for note in notes:
            if note >= test_note and note % test_note == 0 or note < test_note and test_note % note == 0:
                pass
            else:
                final_note = "NO"
                break
        if final_note != "NO":
            break
    # output results
    print "Case #%d: %s" % (cur_case + 1, final_note)
        
# close input file
in_file.close()

    
        
