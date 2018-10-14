# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:14:12 2015

@author: Varun
"""

maxshy = []
audience = []

fh = open("A-small-attempt1.in",'r')
ntc = fh.readline()
for i in range(0,int(ntc)):
    line = fh.readline()
    maxshy.append(line.split(" ")[0])
    audience.append(line.split(" ")[1].strip())
fh.close()
for key in range(0,len(audience)):
    count = 0
    StandPpl = 0
    for i in range(0,len(audience[key])):
        
        if(i == 0  and audience[key][i] == '0'):
            count +=1
            StandPpl +=1
            continue
        if(StandPpl >= int(maxshy[key])):
            break;
        if(StandPpl >= i):
            StandPpl += int(audience[key][i])
        else:
            count +=1
            StandPpl += 1+int(audience[key][i])
    print("Case #"+str(key+1)+": "+str(count))

