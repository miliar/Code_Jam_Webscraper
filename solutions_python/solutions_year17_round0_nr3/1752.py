#!/usr/bin/env python

import math, bisect


# Files
input_file_name = 'C-small-1-attempt0.in'
output_file_name = 'C-small-1-attempt0.out'
# input_file_name = 'C-large.in'
# output_file_name = 'C-large.out'
# input_file_name = 'test.in'
# output_file_name = 'test.out'

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')


# Logic
num_cases = int(input_file.readline())
for case in range(1, num_cases+1):
    [num_stalls, num_people] = map(int, input_file.readline().split())
    num_stalls += 2
    taken_stalls = [1, num_stalls]
    (min_dist, max_dist) = 0, 0
    for k in range(num_people):
        (min_dist, max_dist, new_stall, max_delta) = 0, 0, 0, 0
        for i in range(len(taken_stalls)-1):
            delta = taken_stalls[i+1] - taken_stalls[i] - 1
            if delta > max_delta:
                max_delta = delta
                new_stall = taken_stalls[i] + (delta / 2) + (delta % 2)
                min_dist = new_stall - taken_stalls[i] - 1
                max_dist = taken_stalls[i+1] - new_stall - 1
        bisect.insort(taken_stalls, new_stall)

    # print "Case #" + str(case) + ": " + str(max_dist) + ' ' + str(min_dist)
    output_file.write("Case #" + str(case) + ": " + str(max_dist) + ' ' + str(min_dist) + '\n')


# Clean up
input_file.close()
output_file.close()
