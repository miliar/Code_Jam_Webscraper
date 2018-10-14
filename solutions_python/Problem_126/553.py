#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def solve(case, name, n):
    sum = 0
    for i in range(len(name)):
        consecutive = 0

        for j in range(i + 1, len(name) + 1):
            targetstr = name[i:j]
            bConsecutive = False
            if isVowels(name[j-1]) != True:
                consecutive += 1
                if consecutive >= n:
                    bConsecutive = True
            else:
                consecutive = 0
            
            if len(targetstr) < n:
                continue
            
            if bConsecutive:
                sum += (len(name) - j + 1)
                break

    return "Case #%d: %d\n" % (case, sum) 

def isVowels(cha):
    if cha == "a" or cha == "e" or cha == "i" or cha == "o" or cha == "u":
        return True
    else:
        return False

if __name__ == "__main__":
    isFirst = True
    inData = False

    totalCase = 0
    currentCase = 1 

    for line in inFile.readlines():
        items = line.split()

        # first Line
        if isFirst == True:
            isFirst = False
            totalCase = int(items[0])
            continue
        
        name = items[0]
        n = int(items[1])

        #print solve(currentCase, name, n)
        outFile.write(solve(currentCase, name, n))
        currentCase = currentCase + 1
        if currentCase > totalCase:
            break


