#!/usr/bin/python3

import sys

def minimal_mushrooms(intervals, interval_list):

    #method1
    sol_1 = 0
    for idx in range(1, intervals):
        if interval_list[idx - 1] > interval_list[idx]:
            sol_1 += interval_list[idx - 1] - interval_list[idx]

    #method2
    sol_2 = 0
    max_diff = 0
    for idx in range(1, intervals):
        curr_diff = interval_list[idx - 1] - interval_list[idx]
        if curr_diff > max_diff:
            max_diff = curr_diff

    for idx in range(intervals - 1):
        if interval_list[idx] < max_diff:
            sol_2 += interval_list[idx]
        else:
            sol_2 += max_diff

    return [sol_1, sol_2]


def run():
    name_in = sys.argv[1]
    
    with open(name_in) as file_in:
        test_cases = int(file_in.readline())

        for idx in range(test_cases):
            intervals = int(file_in.readline())
            interval_line = file_in.readline()
            interval_list = [int(x) for x in interval_line.split()]

            ret_list = minimal_mushrooms(intervals, interval_list)

            print("Case #{0}: {1} {2}".format(idx+1, ret_list[0], ret_list[1]))

run()
