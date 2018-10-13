#!/usr/bin/env python

import sys
from string import *

count = 0
total_lines = 0

def calculate(low, high):
    matches = 0

    while low<high:
        low_str = str(low)
        for i in range (1, len(low_str)):
            modified = ''.join([low_str[-i:], low_str[:-i]])
            #print low, high, modified
            modified_str = str(int(modified))
            if int(modified) == high and len(modified_str) == len(str(high)) and len(modified_str) == len(low_str):
                matches += 1
        low += 1
        
    return matches

for line in sys.stdin.readlines():
    if total_lines == 0:
        total_lines = int(line)
        count += 1
    else:
        result = 0
        low, high = line.split(' ')
        low = int(low)
        high = int(high)
        while high > low:
            result += calculate(low, high)
            high -= 1
        print('Case #%d: %s'%(count, result))
        count += 1
