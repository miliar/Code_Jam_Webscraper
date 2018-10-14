#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(case, smax, slist):
    invite = 0
    totalNum = 0
    for i in range(len(slist)):
        num = int(slist[i])
        addNum = 0
        if i == 0:
            if num == 0:
                addNum = 1
        else:
            if totalNum < i:
                addNum = i - totalNum
        totalNum = totalNum +  num + addNum
        invite += addNum
    return "Case #%d: %d\n" % (case, invite) 

if __name__ == "__main__":
    inFile = open("input.txt","r")
    outFile = open("output.txt","w")
    
    isFirst = True
    totalCase = 0
    currentCase = 1 

    for line in inFile.readlines():
        items = line.split()

        if isFirst:
            isFirst = False
            totalCase = int(items[0])
            continue
        else:
            #print solve(currentCase, items[0], items[1])
            outFile.write(solve(currentCase, items[0], items[1]))
            currentCase = currentCase + 1
            if currentCase > totalCase:
                break
    
    inFile.close()
    outFile.close()
    
