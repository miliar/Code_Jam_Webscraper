# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 19:17:05 2017

@author: Rong Huangfu
"""



file_name = 'C:/Users/Rong Huangfu/Google Drive/1. Learning Python/Google Code Jam/A-large.in'

output = 'C:/Users/Rong Huangfu/Google Drive/1. Learning Python/Google Code Jam/A-large_output.out'


with open(file_name, 'rb') as f:
    data = f.readlines()
    data_list = []
    for i in data:
        data_list.append(i.split('\n')[0])
        
output_file = open(output, 'wb')


def flip(cake_str):
    r_str = ''
    for i in range(len(cake_str)):
        if cake_str[i] == '-':
            r_str += '+'
        elif cake_str[i] == '+':
            r_str += '-'
    return r_str
    

def flip_cake(cake, flipper):
    check = 0
    response = 0
    while check == 0:
        print cake
        if cake == '+'*len(cake):
            check = 1
        
        else:
            for i in range(0, len(cake)):
                if cake[i] == '-':
                    if flipper > len(cake)-i:
                        response = 'NA'
                        check = 1
                        break
                        
                    else:
                        cake = cake[:i] + flip(cake[i:i+flipper]) + cake[i+flipper:]
                        response += 1
                        
            
    return response            

            


for i in range(1,len(data_list)):
    data = data_list[i].split(' ')
    cake = data[0]
    flipper = int(data[1])
    
    
    
    
    response = flip_cake(cake, flipper)
    if response == 'NA':
        output_data = 'Case #{}: {}'.format(i, 'IMPOSSIBLE') + '\n'
    else:
        output_data = 'Case #{}: {}'.format(i, response) + '\n'
    print output_data
    output_file.write(output_data)
    #print Case #{}: {}'.format(N, last_n)

output_file.close()
                    

