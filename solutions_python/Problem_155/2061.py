#!/usr/bin/env python
import sys


def read_data():
    input = sys.stdin.read()
    lines = input.split("\n")
    n_times = int(lines[0])
    lines = lines[1:]
    stripped_lines = []
    for line in lines:
        sl = line.strip()
        if sl != "":
            stripped_lines.append(sl)
    assert(n_times == len(stripped_lines))
    return stripped_lines



def convert_string_to_list_of_ints(intstr):
    return [int(d) for d in intstr]



lines = read_data()


def calc_friends(max_shyness, shyness_levels):
    friends_count = 0
    friends_array = [0] * max_shyness
    current_shyness = 0
    for i in range(max_shyness):
        level = shyness_levels[i]

        current_shyness += level - 1

        if current_shyness < 0:
            friends_array[i] = 1
            friends_count += 1
            current_shyness += 1

        #print ("%s %s %s") % (current_shyness, level, friends_count)

    return friends_array, friends_count


case_number = 0
for line in lines:
    case_number += 1

    max_shyness, shyness_levels = line.split()
    max_shyness = int(max_shyness)
    shyness_levels = convert_string_to_list_of_ints(shyness_levels)

    friends_array, friends_count = calc_friends(max_shyness, shyness_levels)

    print "Case #%i: %s" % (case_number, friends_count)
    #print "Case #%i: %s %s %s" % (case_number, friends_array, shyness_levels, friends_count)
