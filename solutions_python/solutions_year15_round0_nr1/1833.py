# -*- coding: utf-8 -*-
# Created on Fri Apr 10 20:24:13 2015
# Implemented in Python 3.4.0
# Author: Yun-Jhong Wu
# E-mail: yjwu@umich.edu

with open('A-large.in', 'r') as dat, open('output.txt', '+w') as output:
    dat.readline()
    for j, line in enumerate(dat):
        _, a = line.split()
        a = list(map(int, list(a)))
        
        count = 0
        current = 0
        for i, s in enumerate(a):
            if current >= i:
                current += s
            else:
                count += i - current
                current = i
                current += s
            
        output.write("Case #{0}: {1}\n".format(j + 1, count))
                
            
            