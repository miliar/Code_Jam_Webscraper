# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:51:48 2015

@author: dxu
"""

import numpy as np


# = 9223372036854775807

def outputStr(case, friends):
    return "Case #"+str(case)+": "+str(friends)+"\n" 

def special(D, plateList, pMove):
    ret_plateList = list(plateList)
    #is the best algo to take the highest plate, split into two,
    #and distribute to an empty plate?
    pMax = max(ret_plateList)
    pMax_ind = ret_plateList.index(pMax)

    #pMove = pMax/2

    #spawn plate only if we need one, otherwise fill the empty plate
    #pMin = min(ret_plateList)
    #if (pMin != 0):
    D+=1
    ret_plateList.append(pMove)
    #else:
    #    pMin_ind = ret_plateList.index(pMin)
    #    ret_plateList[pMin_ind] += pMove
    ret_plateList[pMax_ind] -= pMove
    
    return D, ret_plateList

def solvePancake(time, D, plateList):
    #is there a faster path? if so, give up
    #print _bestTime
    global _bestTime
    if (time > _bestTime):
        return _bestTime
    
    #are there any pancakes left?
    if isComplete(plateList):
        if (time < _bestTime):
            _bestTime = time
        return time

    #print 'we on time: ' + str(time)
    #increment time
    time += 1;
    
    #eat time   
    eatTime = solvePancake(time, D, eat(plateList))

    #see if we can end this with an eat. (you can't finish on a special)
    if (eatTime == time):   
        return eatTime

    #we should really only perform a special if  max(plateList) > D
    #if (max(plateList) > D):

    #special time if possible
    if ((max(plateList) > 1) and (max(plateList) != 2)):
        specialTimeList = []
        for platesToMove in range(2, (max(plateList)/2)+2):
            spec_D, spec_plateList = special(D, plateList, platesToMove)    
            specialTimeList.append(solvePancake(time, spec_D, spec_plateList))

        #compare eat time to special time, and return the better one.
        if (eatTime > min(specialTimeList)):
            return min(specialTimeList)
        else:
            return eatTime
    else:
        return eatTime
    #else:
    #    return eatTime
    
def eat(plateList):
    #print 'eat ' + str(len(plateList))
    #print plateList
    ret = list(plateList)
    for i in range(0, len(ret)):
        if ret[i] > 0:
            ret[i] -= 1
    return ret

def isComplete(plateList):
    pLeft = 0;
    for i in range(0, len(plateList)):
        pLeft += plateList[i]
    return (pLeft==0)

    
with open('input.txt') as input:
    content = input.readlines()

T = int(content[0])

text_file = open("output.txt", "w")

#T = 1 #TEMP
for i in range(1,T+1):
    D = int(content[i*2-1])
    line = content[i*2]
    print i
    lineList = line.strip().split(' ');
    print lineList
    
    #turn list strs into ints
    lineList = map(int, lineList)

    startTime=0
    _bestTime = 9223372036854775807
    smallestTime = solvePancake(startTime, D, lineList)
    
    #output
    text_file.write(outputStr(i, smallestTime))
    
