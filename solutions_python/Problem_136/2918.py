#!/usr/bin/python

import sys

def optimize(num, args):
    c = args[0]
    f = args[1]
    x = args[2]

    cur_rate = 2.0
    cur_time = 0.0
    cur_best = cur_time + x / cur_rate
    cur_farm = c / cur_rate
    best = cur_best
    while (True):
        # check if adding cookie farm helps
        next_rate = cur_rate + f
        next_time = cur_time + cur_farm 
        next_best = next_time + x / next_rate
        next_farm = c / next_rate
        best = min(best, min(cur_best, next_best))

        if next_best > cur_best:
            break
        cur_rate = next_rate
        cur_time = next_time
        cur_best = next_best
        cur_farm = next_farm

    print 'Case #%d: %.7f' % (num + 1, best)

def parse_input(file_pointer):
    lines = file_pointer.readlines()
    num_cases = int(lines[0])
    for i in range(num_cases):
        args = [float(j) for j in lines[i + 1].split(' ')]
        optimize(i, args)

def read_file(file_name):
    return open(file_name, 'r')

# main
file_pointer = read_file(sys.argv[1])
parse_input(file_pointer)
