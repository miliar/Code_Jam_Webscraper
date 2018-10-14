# -*- coding: utf-8 -*-
# Created on Fri Apr 10 20:24:13 2015
# Implemented in Python 3.4.0
# Author: Yun-Jhong Wu
# E-mail: yjwu@umich.edu


with open('D-small-attempt1.in', 'r') as dat, open('output.txt', '+w') as output:
    dat.readline()
    for s, line in enumerate(dat):
        x, r, c = map(int, line.split())
        ans = ''
        if r * c % x:
            ans = "RICHARD"
            
            
        elif x <= 2:
            ans = "GABRIEL"
        elif r == 1 or c == 1 or (r < x and c < x):
            ans = "RICHARD"

        elif x == 3:
            ans = "GABRIEL"
            
        elif x == 4 and ((r, c) == (2, 4) or (r, c) == (4, 2)):            
            ans = "RICHARD"
        else:            
            ans = "GABRIEL"

            
        output.write("Case #{0}: {1}\n".format(s + 1, ans)) 
        
                
            
            