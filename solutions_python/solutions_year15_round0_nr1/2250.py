#!/usr/bin/env python3

import sys

# Inital line number is amount of cases to read
def get_required_friends(shyness_string):
    required_friends = 0
    total_applause = int(shyness_string[0])
    for si_index in range(1,len(shyness_string)):
        if(si_index > total_applause):
            friend_difference = si_index-total_applause 
            required_friends += friend_difference
            total_applause += friend_difference
        total_applause += int(shyness_string[si_index])

    return required_friends



name, input_file, output_file = sys.argv
f = open(input_file, 'r')
w = open(output_file, 'w')

cases = int(f.readline().rstrip('\n'))

for cur_case in range(1,cases+1):
    shyness_levels = f.readline().rstrip('\n')
    print(shyness_levels)
    num, shyness_levels = shyness_levels.split()
    required_friends = get_required_friends(shyness_levels)
    print("Case #%d: %d" % (cur_case, required_friends))
    write_str = "Case #" + str(cur_case) + ": " + str(required_friends) + "\n"
    w.write(write_str)


