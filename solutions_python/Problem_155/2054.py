#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
output = []
contents = contents[1:]
for case in range(1,num_cases+1):
    max_val, vals = contents[0]
    contents = contents[1:]
    max_val = int(max_val)
    val_list = [int(a) for a in vals]
    total = 0
    added = 0
    index = 0
    while index <= max_val:
        #print index, total, added
        if total >= max_val:
            break
        total += val_list[index]
        #print total
        temp_index = index + 1
        while temp_index <= max_val:
            if val_list[temp_index] == 0:
                temp_index += 1
            else:
                break
        if total < temp_index:
            added += (temp_index - total)
            total = temp_index
        index = temp_index
    results = added
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %i" % results)

write_output(output)


