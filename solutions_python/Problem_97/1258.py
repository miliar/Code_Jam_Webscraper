#!/usr/bin/env python
import os

#get list of all recycled numbers of a given number
def getRecycleNumbers(num, B, uniquRecyclePairs):
    
    lstNums = []
    
    for i in range(1, len(num)):
        rear = num[i:]
        front = num[0:i]
        recycleNum = (rear + front)
        
        #check valid range
        if (int(recycleNum) > B) or (int(recycleNum) <= int(num)):
            continue
        
        lstNums.append(recycleNum)
        uniquRecyclePairs.add((num, recycleNum))
        
    return lstNums




#Given integers A and B with the same number of digits
#and no leading zeros, how many distinct recycled pairs (n, m) are there with A ? n < m ? B?
def getDistinctRecycleNumbers(A, B):
    
    uniquRecyclePairs = set()
    
    #iterate in range and collect unique pairs
    for num in range(A, B + 1):
        getRecycleNumbers(str(num), B, uniquRecyclePairs)

    #print uniquRecyclePairs
    return len(uniquRecyclePairs)





# take lsit of test cases and outputs list of corresponding answers
def solveRecycleProblem(lstRange):
    
    outputNums = []
    
    #iterate in range and collect unique pairs
    for case in lstRange:
        outputNums.append(getDistinctRecycleNumbers(int(case[0]), int(case[1])))

    return outputNums





#take input from file
def problemIO(inputFile):
    text = open(inputFile, "rb").read()
    lines = text.split("\n")
    
    #take first line - no. of test cases
    cases = int(lines[0].strip())
    
    #DS
    lstRange = []
    
    #handle each test case
    for line in lines[1:]:
        
        if(line.strip()):
            range = line.split(" ")
            lstRange.append((range[0].strip(), range[1].strip()))
        
    return lstRange






#print output to file
def formatOutput(outputFile, lstStrings):
    F = open(outputFile, "wb")
    
    for i in range(0, len(lstStrings)):
        out = "Case #" + str(i + 1) + ": " + str(lstStrings[i])
        print out
        F.write(out + "\r\n")
    
    F.close()
    




#unit tests
if __name__ == '__main__':
    fileLoc = "C:\\Users\\manish_ramani\\Dropbox\\projects\\google_codejam\\"
    
    #takes input file and gets range for each case
    lstRange = problemIO(fileLoc + "C-small-attempt0.in")
    
    #solves the problem
    outputLst = solveRecycleProblem(lstRange)
    
    #write output to file
    formatOutput(fileLoc + "recycleOutput.out", outputLst)
    
    #print getRecycleNumbers("12345")
    #print getDistinctRecycleNumbers(1111, 2222)
    
