#!/bin/python3
# -*- coding:utf-8 -*-

import math

def kaibun(integerstr):
    lenstr = len(integerstr)
    for i in range(0, int(lenstr/2)):
        if(integerstr[i] != integerstr[lenstr -i -1]):
            return 0
    
    return 1



def fairsquare(integerstr):
    num1 = int(integerstr)
    num2 = math.sqrt(num1)
    
    if(num2 != int(num2)):
        return 0
    
    result1 = kaibun(str(int(num2)))
    
    if(result1 == 1):
        if(kaibun(str(num1)) == 1):
            return 1
    
    return 0


filo = open('C-small-attempt0.in')
alllines = filo.readlines()
filo.close()

T = int(alllines[0])

#print(T, end="")

index = 1

for i in range(1, T+1):
    line1 = alllines[i].rstrip()
    lintinteget = line1.rsplit(" ")
    minint = lintinteget[0]
    maxint = lintinteget[1]
    
    result = 0
    for n in range(int(minint), int(maxint)+1):
        result += fairsquare(str(n))
    
    print("Case #" + str(index) + ": " + str(result))
    index += 1



