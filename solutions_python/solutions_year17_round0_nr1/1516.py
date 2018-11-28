# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:05:33 2017

@author: Ameet
"""

def pancake_flips(pancakes, K):
    pancakes_list = list(pancakes)
    flips = 0
    while '-' in pancakes_list:
        first_unhappy = pancakes_list.index('-')
        if first_unhappy > len(pancakes_list)-K:
            return "IMPOSSIBLE"
        else:
            for i in range(first_unhappy,first_unhappy+K):
                pancakes_list[i] = '-' if pancakes_list[i]=='+' else '+'
            flips += 1
    
    return str(flips)
    



def run_sample(input_filename, output_filename, func):
    input_file = open(input_filename, 'r')
    num_tests_line = input_file.readline()
    num_tests = int(num_tests_line)
    test_number = 1
    output_file = open(output_filename, 'w')
    for line in input_file:
        [pancakes, K] = line.split(" ")
        K = int(K)
        output = func(pancakes, K)
        output_file.write("Case #")
        output_file.write(str(test_number))
        output_file.write(": ")
        output_file.write(output)
        output_file.write("\n")
        test_number += 1


    