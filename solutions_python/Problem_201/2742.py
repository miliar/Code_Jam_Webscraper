# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 16:20:32 2017

@author: Suganya
"""
from itertools import groupby

f = open('C-small-1-attempt0.in')
f1 = open('out.txt', 'wb')
lines = f.read().split("\n")
num_lines = len(lines)
k = int(lines[0])
for j in range(1,k+1):
    line = lines[j].split(" ")
    no_of_baths = int(line[0])
    people = int(line[1])
    baths = [0] * (no_of_baths+2)
    baths[0] = 1
    baths[no_of_baths+1] = 1
    for i in range(0, people):
        s = ''.join(str(y) for y in baths)
        groups = groupby(s)
        result = [(int(label), sum(1 for _ in group)) for label, group in groups]
        index = 0
        max_count = 0
        max_index = 0
        l = 0
        max_len = 0
        for a,count in result:
            res_len = len(result)
            if count > max_count and a == 0:
                max_count = count
                max_index = index
                max_len = l
            index = index + count
            l = l+1
        if(max_count % 2 != 0):
            baths[max_index+(max_count/2)] = 1
        if(max_count % 2 == 0):
            baths[max_index+(max_count/2 - 1)] = 1
                  
        if(max_count % 2 == 0):
            ls = max_count / 2
            rs = ls - 1
        else:
            ls = max_count / 2
            rs = ls
    output = 'Case #'+ str(j) + ': ' + str(ls) + ' ' + str(rs)
    f1.write(output)
    f1.write('\n')
    print(output)
        
f.close()
f1.close()