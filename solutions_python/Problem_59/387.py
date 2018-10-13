import math
import re

def doSomething(a, b):
    ans = 0

    ans = a + b
    
    return ans

#inputPath = "Input.txt"
#inputPath = "A-small-attempt1.in"
inputPath = "A-large.in"

inFile = open(inputPath, "r")
outFile = open("Output.txt", "w")

lines = inFile.readlines()

cases = int(lines[0])

index = 1
for i in range(0, cases):
    meta = lines[index]
    metaArr = meta.split(" ")
    
    N = int(metaArr[0])
    M = int(metaArr[1])
    
    index = index + 1
    
    #existing = []
    
    #for i in range(0, N):        
        #existing.append(str.rstrip(lines[index], "\n"))
        #index = index + 1
        
    #new = []
    
    #for i in range(0, M):
        #new.append(str.rstrip(lines[index], "\n"))
        #index = index + 1
    if i == 5:
        test = ""
    existing = dict()
    for j in range(0, N):
        curr = str.rstrip(lines[index], "\n")
        index = index + 1
        arr = curr.split("/")
         
        currDict = existing
        for k in range(1, len(arr)):
            #print arr[k], existing, currDict
            if arr[k] not in currDict:
                currDict[arr[k]] = dict()            
            currDict = currDict[arr[k]]
            #print arr[k], existing, currDict
    count = 0
    
    for j in range(0, M):
        curr = str.rstrip(lines[index], "\n")
        index = index + 1
        arr = curr.split("/")
        
        currDict = existing
        for k in range(1, len(arr)):
            #print arr[k], existing, currDict
            if arr[k] not in currDict:
                currDict[arr[k]] = dict()
                count = count + 1
            
            currDict = currDict[arr[k]]
    
    #print N, M, count, existing
    
    outFile.write("Case #" + str(i+1) + ": " + str(count) + "\n")
print "Finished"