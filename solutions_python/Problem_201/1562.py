# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:05:33 2017

@author: Ameet
"""
from math import ceil, floor


def stall_split(N,K):
    left_block_size = 0
    right_block_size = 0
    block_size_freqs = {N: 1}
    while K>0:
        max_block_size = max(block_size_freqs.keys())
        max_block_freq = block_size_freqs.pop(max_block_size)
        
        left_block_size = floor((max_block_size-1)/2)
        right_block_size = ceil((max_block_size-1)/2)
        block_size_freqs[left_block_size] = block_size_freqs.get(left_block_size,0) + max_block_freq
        block_size_freqs[right_block_size] = block_size_freqs.get(right_block_size,0) + max_block_freq
        
        K -= max_block_freq
            
    return str(right_block_size) + " " + str(left_block_size)
            
        


def run_sample(input_filename, output_filename, func):
    input_file = open(input_filename, 'r')
    num_tests_line = input_file.readline()
    num_tests = int(num_tests_line)
    test_number = 1
    output_file = open(output_filename, 'w')
    for line in input_file:
        [N, K] = line.split(" ")
        N = int(N)        
        K = int(K)
        output = func(N, K)
        output_file.write("Case #")
        output_file.write(str(test_number))
        output_file.write(": ")
        output_file.write(output)
        output_file.write("\n")
        test_number += 1


    