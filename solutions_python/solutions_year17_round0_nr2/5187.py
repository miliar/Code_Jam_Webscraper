#!/usr/bin/python3
import sys

fileName = sys.argv[1]
print(fileName)
inputFile = open(fileName, 'r')
lines = inputFile.readlines()
inputFile.close()

def isTidyNum(n):
    numStr = str(n)
    for i in range(0, len(numStr)-1):
        if numStr[i] > numStr[i+1]:
            return False
    return True

skip = True
count = 1
for num in lines:
    if skip == True:
        skip = False
        continue
    for currNum in range(int(num), 0, -1):
        if isTidyNum(currNum):
            print("Case #%d: %d" %(count, currNum))
            break
    count += 1
