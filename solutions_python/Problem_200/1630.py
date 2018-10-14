# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:44:38 2017

@author: Ameet
"""

import math

def max_tidy_num(N):
    remaining = N
    return_value = 0
    if N==0:
        return 0
    num_digits = int(math.log10(remaining))+1
    while num_digits > 0:
        first_digit = remaining // 10**(num_digits-1)
        if first_digit >= return_value % 10:
            return_value *= 10
            return_value += first_digit
            remaining = remaining % 10**(num_digits-1)
            num_digits -= 1
        else:
            remaining = max_tidy_num(return_value*10**(num_digits) - 1)
            return max_tidy_num(remaining)
    return return_value



def run_sample(input_filename, output_filename, func):
    input_file = open(input_filename, 'r')
    num_tests_line = input_file.readline()
    num_tests = int(num_tests_line)
    test_number = 1
    output_file = open(output_filename, 'w')
    for line in input_file:
        N = int(line)
        output = func(N)
        output_file.write("Case #")
        output_file.write(str(test_number))
        output_file.write(": ")
        output_file.write(str(output))
        output_file.write("\n")
        test_number += 1


    