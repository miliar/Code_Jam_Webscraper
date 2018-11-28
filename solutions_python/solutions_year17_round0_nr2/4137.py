# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 11:02:36 2017

@author: User
"""

import sys

# Read product data from file
def read_data_from_file(fn):
    
    n_cases = 0
    last_num = []
    
    n_line = 0

    with open(fn) as file:
        for line in file:
            if n_line == 0:
                n_cases = int(line)
                n_line += 1
            else:
                last_num.append(int(line))
                
    return n_cases, last_num


def write_output_to_file(file_name, n_cases, output):
    data = ""
    for ii in range(0, n_cases):
        data += 'Case #{}: {}\n'.format((ii + 1), output[ii])
                
    with open(file_name, "w") as f:
        f.write(data)
    
    print('Wrote data to {}'.format(file_name))
    f.close()


def check_array(num_arr):
    for ii in range(0, len(num_arr)):
        if ii < (len(num_arr) - 1):
            if num_arr[ii] > num_arr[ii + 1]:
                num_arr[ii] = num_arr[ii] - 1
                
                for jj in range(ii + 1, len(num_arr)):
                    num_arr[jj] = 9
                           
                check_array(num_arr)
    return num_arr


def find_previous_tidy(num):
    num_arr = [int(x) for x in str(num)]
    
    check_array(num_arr)
                
    return int(''.join(map(str, num_arr)))

file_name = 'B-large.in'
#file_name = 'example.txt'
output_file_name = 'output_large.txt'
#output_file_name = 'output.txt'
num_cases, last_num = read_data_from_file(file_name)
output = []

for case in range(0, num_cases):
    n = last_num[case]
    tidy_num = find_previous_tidy(n)
    output.append(tidy_num)
    
write_output_to_file(output_file_name, num_cases, output)