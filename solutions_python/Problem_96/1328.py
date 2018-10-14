# Problem B
#
# Google Code Jam 2012
# CWSFDavid
#

import math

file_in = list(open('B-small.in', 'r'))
file_in = file_in[1:]

count = 0
output = []
for case in file_in:
    count += 1
    case = case[:-1].split()
    special = int(case[1])
    goal = int(case[2])
    if goal > 1:
        goal_min = goal * 3 - 2
        goal_abs_min = goal * 3 - 4

    elif goal == 1:
        goal_min = 1
        goal_abs_min = 1

    else:
        goal_min = 0
        goal_abs_min = 0

    temp = case[3:]
    tally = 0
    for score in temp:
        score = int(score)
        if score >= goal_min:
            tally += 1

        elif score >= goal_abs_min and special > 0:
            tally += 1
            special -= 1            

    print 'Case #' + str(count) + ': ' + str(tally)


