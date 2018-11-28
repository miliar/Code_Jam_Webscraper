#!/usr/bin/python

"""
Bot Trust problem solution
(GCJ 2011, Qualification Round)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: bot_trust.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    test_line = in_file.readline().split(" ")
    N = int(test_line[0])
    sequence = []
    for i in range(N):
        sequence.append((test_line[i*2+1], int(test_line[i*2+2])))
    # begin modelling
    type_map = {"O": False, "B": True}
    time = {False: 0, True: 0}
    position = {False: 1, True: 1}
    for bot_type, button_num in sequence:
        bot_type = type_map[bot_type]
        time_saving = 0
        if time[bot_type] < time[not bot_type]:
            time_saving = time[not bot_type] - time[bot_type]
        time_required = abs(position[bot_type] - button_num)
        time[bot_type] = max(time[True], time[False]) + max(0, time_required - time_saving) + 1
        position[bot_type] = button_num
    print "Case #%d: %s" % (cur_case + 1, max(time[True], time[False]))

# close input file
in_file.close()

    
        
