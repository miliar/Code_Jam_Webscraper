#!/usr/bin/env python
# -*- coding: utf-8  -*-

import sys
import os

input_path = sys.argv[1]
output_path = sys.argv[2]

def do_algorithm(test_idx, input_file, output_file):
    line = input_file.readline()
    words = line.split()
    C = float(words[0])
    F = float(words[1])
    X = float(words[2])

    cost = X / 2.0
    farm_num = 1.0
    farm_accum_cost = 0.0
    cookie_price = 2.0

    while True:
        farm_cost = farm_accum_cost + C / cookie_price 
        farm_accum_cost = farm_cost
        cookie_price = cookie_price + F 
        cookie_cost = X / cookie_price
        new_cost = farm_cost + cookie_cost

        if cost < new_cost:
            break
        else:
            cost = new_cost

    # Answer
    output_file.write('Case #%d: ' % test_idx + str(format(cost, '.7f')) + '\n')

try:
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')

    test_num = int(input_file.readline())
    for i in range(test_num):
        do_algorithm(i+1, input_file, output_file)

    input_file.close()
    output_file.close()
except Exception as e:
    print str(e)
    sys.exit(-1)
