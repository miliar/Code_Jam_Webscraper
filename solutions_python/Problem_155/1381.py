# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:51:48 2015

@author: dxu
"""

with open('input.txt') as input:
    content = input.readlines()

def outputStr(case, friends):
    return "Case #"+str(case)+": "+str(friends)+"\n" 

T = content[0]

text_file = open("output.txt", "w")
for i in range(1, len(content)):
    lineList = content[i].split(' ');
    Smax = lineList[0]
    
    #if Smax = 0
    if (len(lineList) == 1):
        text_file.write(outputStr(i, 0))
        continue
    
    pplStr = lineList[1].strip()
    sum_addPpl = 0
    pplStanding = int(pplStr[0])
    for si in range(1, len(pplStr)):
        if pplStanding >= si:
            pplStanding += int(pplStr[si])
        else:
            addPpl = si - pplStanding
            sum_addPpl += addPpl
            pplStanding += addPpl + int(pplStr[si])

    #output
    text_file.write(outputStr(i, sum_addPpl))