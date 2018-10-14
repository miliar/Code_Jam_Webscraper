#!/usr/bin/python

"""
RPI problem solution
(GCJ 2011, Round 1B)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: rpi.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    N = int(in_file.readline())
    schedule = []
    for i in range(N):
        schedule.append(in_file.readline().strip())
    # calculating WPs
    wps = []
    wins = []
    totals = []
    for command in schedule:
        win = command.count("1")
        total = win + command.count("0")
        wins.append(win)
        totals.append(total)
        wps.append(float(win) / float(total))
    # calculating OWPs
    owps = []
    for i in range(N):
        wp_cur = 0
        for j in range(N):
            if j != i:
                if schedule[j][i] != ".":
                    win_cur = wins[j]
                    total_cur = totals[j] - 1
                    if schedule[j][i] == "1":
                        win_cur -= 1
                    wp_cur += float(win_cur) / float(total_cur)
        owps.append(wp_cur / totals[i])
    # calculating OOWPs
    oowps = []
    for i in range(N):
        owp_cur = .0
        for j in range(N):
            if j != i:
                if schedule[j][i] != ".":
                    owp_cur += owps[j]
        oowps.append(owp_cur / float(totals[i]))
    # output results
    print "Case #%d:" % (cur_case + 1, )
    for i in range(N):
        rpi = 0.25 * wps[i] + 0.5 * owps[i] + 0.25 * oowps[i]
        print rpi
# close input file
in_file.close()

    
        
