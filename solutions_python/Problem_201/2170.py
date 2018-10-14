# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:20:57 2017

@author: lucap
"""
import numpy as np

def constraints_inefficient(spaces, people):
    segments = [spaces]
    
    while(people > 1):
        max_seg = max(segments)
        segments.remove(max_seg)
        segments.append(int((max_seg - 1)/2))
        segments.append(int(max_seg/2))
        people -= 1
    
    return [int((max(segments) - 1)/2), int(max(segments)/2)]

def constraints(spaces, people):
    if (people == 1):
        return [int((spaces-1)/2), int(spaces/2)]
    
    if (people % 2 == 0):
        return constraints(int(spaces/2), int(people/2))
    
    return constraints(int((spaces - 1)/2), int((people - 1)/2))


file = open("C:\\Users\\lucap\\Documents\\Python\\Code Jam 2017\\C_small_2_stalls.in", 'r')
file_out = open("C:\\Users\\lucap\\Documents\\Python\\Code Jam 2017\\outputsmall2_STALLS.txt", 'w')
tmp_file = file.read().splitlines()
file.close()

cases = int(tmp_file[0])    
        
for i in range(1, cases + 1):
    spaces, people = [int(s) for s in tmp_file[i].split(" ")]
    low, high = constraints(spaces, people)
    print("Case #{}: {} {}".format(i, high, low), file = file_out)
    
file_out.close()
    