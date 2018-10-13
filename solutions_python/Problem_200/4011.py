# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 19:17:05 2017

@author: Rong Huangfu
"""

file_name = 'C:/Users/Rong Huangfu/Google Drive/1. Learning Python/Google Code Jam/A-small-practice.in'

file_name = 'C:/Users/Rong Huangfu/Google Drive/1. Learning Python/Google Code Jam/B-small-attempt0.in'

output = 'C:/Users/Rong Huangfu/Google Drive/1. Learning Python/Google Code Jam/B-small-attempt0_output.out'


with open(file_name, 'rb') as f:
    data = f.readlines()
    data_list = []
    for i in data:
        data_list.append(i.split('\n')[0])
        
output_file = open(output, 'wb')


def check_tidy(number):
    str_ = str(number)
    check = 0
    for i in range(1, len(str_)):
        if int(str_[i]) < int(str_[i-1]):
            check = 1
    return check


for i in range(1,len(data_list)):
    data = int(data_list[i])
    check = 1
    while check==1:
        number_test = check_tidy(data)
        if number_test == 1:
            data = data - 1
        elif number_test == 0:
            response = data
            check = 0

    output_data = 'Case #{}: {}'.format(i, response) + '\n'
    print output_data
    output_file.write(output_data)
    #print Case #{}: {}'.format(N, last_n)

output_file.close()
                    

