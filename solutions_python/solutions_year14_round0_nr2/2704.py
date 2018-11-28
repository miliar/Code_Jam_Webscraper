#! /usr/bin/python

import sys

#
# Main
#
if len(sys.argv) != 2:
    print 'Incorrect arguments'
    sys.exit(0)

fh = open(sys.argv[1])

# Read number of test cases from the file
n_tests = int(fh.readline())

for i in range(1, n_tests + 1):
    fields = fh.readline().rstrip().split()
    cost = float(fields[0])
    add_cps = float(fields[1])
    goal = float(fields[2])

    elapsed_time = 0.0
    curr_cps = 2.0

    while 1:    
        time_to_goal = goal / curr_cps
        time_to_buy = cost / curr_cps
        time_to_goal_if_bought = time_to_buy + (goal / (curr_cps + add_cps))

        #print 'Time to goal', time_to_goal
        #print 'Time to buy', time_to_buy
        #print 'Time to goal if bought', time_to_goal_if_bought

        if time_to_goal < time_to_goal_if_bought:
            elapsed_time += time_to_goal
            break
        else:
            elapsed_time += time_to_buy
            curr_cps += add_cps


    print 'Case #{0}: {1:.7F}'.format(i, elapsed_time)

