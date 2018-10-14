# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:59:21 2015

@author: abdou_bms
"""

    

f = open("A-large.in","r")
f1 = open("A-large.out","w")
a = int(f.readline())
for i in range(a):
    #################
    line = f.readline()
    line = line[0:len(line)-1]
    line = line.split()
    maxShy = int(line[0])
    string = line[1]
    #################
    j = len(string)
    x=j-1
    l = list()
    friends=0
    while(x>=0):
        clappers = 0
        for k in range(x):
            clappers = clappers + int(string[k])
        l.extend([x - clappers])
        x=x-1   
    print l
    friends = max(l)
    f1.write("Case #"+str(i+1)+": "+str(friends)+"\n")
f.close()
f1.close()