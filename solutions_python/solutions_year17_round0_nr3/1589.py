#!/usr/bin/python

casenumber = int(raw_input())
stallStateMap = {}

def findLeftMostEmptyStall():
    leftMostMax = 0;
    for x in stallStateMap.keys():
        if x > leftMostMax:
            leftMostMax = x
    return leftMostMax


for case in range(0, casenumber):
    n, k = [int(s) for s in raw_input().split(" ")]
    stallStateMap.clear()
    stallStateMap[n]=1
    min=0
    max=0
    for people in range(0,k):
        theMax = findLeftMostEmptyStall()
        if stallStateMap[theMax] == 1:
            del stallStateMap[theMax]
        else:
            stallStateMap[theMax] -= 1;
        if theMax / 2 * 2 == theMax:
            max = theMax / 2
            min = theMax / 2 - 1
            if stallStateMap.has_key(max):
                stallStateMap[max] += 1
            else:
                stallStateMap[max] = 1
            if stallStateMap.has_key(min):
                stallStateMap[min] += 1
            elif min > 0:
                stallStateMap[min] = 1
        else:
            min = max = theMax / 2
            if min > 0:
                if stallStateMap.has_key(min):
                    stallStateMap[min] += 2
                else:
                    stallStateMap[min] = 2
        #print stallStateMap
 

    print "Case #{}: {} {}".format(case+1,max,min)