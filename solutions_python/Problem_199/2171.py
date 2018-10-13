# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:04:39 2017

@author: lucap
"""
def convert_string(arrangement):
    num_arrangement = []
    
    for i in arrangement:
        if(i == '+'):
            num_arrangement.append(1)
        else:
            num_arrangement.append(0)
    
    return num_arrangement
            
def count_overflip(arrangement, size):
    count = 0
    index = 0
    states = convert_string(arrangement)
    
    for i in range(len(states)):   

        if(states[i] == 1):
            continue
        
        if(i > len(states) - size):
            return -1
        
        for k in range(size):
            states[i + k] = 1 if states[i + k] == 0 else 0
        
        count += 1
    
    return count

file = open("C:\\Users\\lucap\\Documents\\Python\\Code Jam 2017\\A_large_oversize.in", 'r')
file_out = open("C:\\Users\\lucap\\Documents\\Python\\Code Jam 2017\\output_OVERSIZEFLIP.in", 'w')
tmp_file = file.read().splitlines()
file_in.close()

cases = int(tmp_file[0])    
        
for i in range(1, cases + 1):
    arr, size = [s for s in tmp_file[i].split(" ")]
    n = count_overflip(arr, int(size))
   
    if (n >= 0):
        print("Case #{}: {}".format(i, n), file = file_out)
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"), file = file_out)
    
file_out.close()
        
        