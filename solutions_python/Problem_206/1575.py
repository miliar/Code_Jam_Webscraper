# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:08:04 2017

@author: vushesh
"""

with open("D:/Studies/Online Competitions/Google codejam/A-large.in" ,"r") as f:
    lines = f.readlines()

f.close()    

t = int(lines[0])

with open("D:/Studies/Online Competitions/Google codejam/Aoutput.txt" ,"w") as f:
    count = 1
    for outer in range(1,t+1):
        d , n = lines[count].split(' ')
        d = int(d)
        n = int(n)
        count +=1
        value = -1
        for loop in range(0,n):
            x , y = lines[count].split(' ')
            x = int(x)
            y = int(y)
            count +=1
            temp = (d - x)/y
            value = max(temp,value)
         
        ans = d/value 
        y = "%.6f" % ans 
        x = "Case #"+str(outer)+": "+str(y)    
        f.write(x)
        f.write("\n")


