# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:18:07 2015

@author: guy
"""

infile = open('1.in','r')
n = []
s = []
Stop = True
for line in infile:
    if not Stop:
        n.append(list(map(int,line.split(' ')))[0])
        s.append(line.split(' ')[1])
    Stop = False
        
        
for i in range(len(s)):
    s[i] = ''.join(s[i].split('\n'))
    s[i] = list(map(int,list(s[i])))
    
    
    
    

def answer(values):
    peopleAboveOrBelow= 0
    currentNumPeople = 0
    for num in values:
        if peopleAboveOrBelow < 0:
            currentNumPeople += 1
            peopleAboveOrBelow += 1
        peopleAboveOrBelow += num-1
    return currentNumPeople
            
outfile = open('1.out','w')
for i in range(len(s)):
    outfile.write("Case #{0}: {1}\n".format(i+1,answer(s[i])))
outfile.close()