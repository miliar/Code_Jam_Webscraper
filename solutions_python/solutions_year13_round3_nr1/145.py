#!/usr/bin/python

import re
import sys
from string import maketrans

input_file = open('A-large.in')
output_file = open('A-large.out', 'w')

T = int(input_file.readline())

cons = set("qwrtzpsdfghjklyxcvbnm")


for t in range(T):
    name, n = input_file.readline().split(' ')
    L = len(name)
    n = int(n)
    
    n_value = 0
    
    nums = [0 for c in name]
    nums[0] = (1 if name[0] in cons else 0)
    
    for i in xrange(1, len(name)):
        if name[i] in cons:
            nums[i] = nums[i-1] +1
        else:
            nums[i] = 0
            
    indexes = []
    for i in xrange(len(nums)):
        if nums[i] >= n: indexes.append(i)
        
    for i in xrange(len(indexes)-1):
        n_value += (indexes[i] - n +2) * (indexes[i+1]-indexes[i])
    
    if len(indexes) > 0:
        n_value += (indexes[-1] - n +2) * (L-indexes[-1])
    
    
    result = str(n_value)
    output_file.write("Case #" + str(t + 1) + ": " + result + "\n")
    

input_file.close()
output_file.close()
