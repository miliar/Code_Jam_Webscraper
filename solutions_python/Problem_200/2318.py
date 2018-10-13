# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:53:51 2017

@author: lucap
"""
def is_tidy(num):
    
    digits = []
    
    while(num > 0):
        digits.append(num % 10)
        num = int(num/10)
    
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i + 1]:
            continue
        
        return False
    
    return True

def largest_tidy(limit):
    
    while(limit > 0):
        if(is_tidy(limit)):
            return limit
        
        limit -= 1
    
    return 0

file_in = open("C:\\Users\\lucap\\Documents\\Python\\Code Jam 2017\\B_small_TIDY.in", 'r')
file_out = open("C:\\Users\\lucap\\Documents\\Python\\Code Jam 2017\\outputsmall_TIDY.txt", 'w') 

tmp_file = file_in.read().splitlines()
file_in.close()

cases = int(tmp_file[0])

for i in range(1, cases + 1):
    print("Case #{}: {}".format(i, largest_tidy(int(tmp_file[i])), file = file_out))
    
file_out.close()