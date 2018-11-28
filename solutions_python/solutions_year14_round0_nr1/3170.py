'''
Created on 12-Apr-2014

@author: Pankaj
'''
import os, sys

def getCases(numCases, inputData):
    cases = list()
    for i in range(numCases):
        j = i*10
        firstChoice = inputData[j]
        firstArr = inputData[j+1:j+5]
        secondChoice = inputData[j+5]
        secondArr = inputData[j+6:j+10]
        cases.append((firstChoice, firstArr, secondChoice, secondArr))
    return cases

def solveCase(firstChoice, firstArr, secondChoice, secondArr):
    options = firstArr[int(firstChoice)-1][:-1].split(" ")
    secondOption = secondArr[int(secondChoice)-1][:-1].split(" ")
    found = 0
    num = 0
    for each in options:
        if each in secondOption:
            found += 1
            num = each
    if not found:
        return "Volunteer cheated!"
    if found > 1:
        return "Bad magician!"
    return num
        
inputFile = sys.argv[1]
fileHandle = file(inputFile, "r")
fileData = fileHandle.readlines()
fileHandle.close()

nTests = int(fileData[0].replace("\n", "").replace(" ", ""))

outputFile = os.path.splitext(inputFile)[0] + ".out"
if os.path.exists(outputFile):
    os.remove(outputFile)
fileHandle = file(outputFile, "w")

cases = getCases(nTests, fileData[1:])

for i, eachCase in enumerate(cases):
    (firstChoice, firstArr, secondChoice, secondArr) = eachCase
    result = solveCase(firstChoice, firstArr, secondChoice, secondArr)
    fileHandle.write("Case #%d: %s\n" % (i+1, result))
fileHandle.close()
