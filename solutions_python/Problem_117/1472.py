#!/usr/bin/python
import sys

def getHighestGrass(lawnLine):
    highest = 0
    for num in lawnLine:
        if num > highest:
            highest = num
    return highest

def solveCase(lawn, width, height):
    testlawn = [[100 for i in range(width)] for j in range(height)]
    for column in range(0,height):
        # for each horizontal row, try applying the heighest grass amount for that row to each one
        highestGrass = getHighestGrass(lawn[column])
        for row in range(0,width):
            testlawn[column][row] = highestGrass
    
    for row in range(0,width):
        # for each vertical column, try applying the heighest grass amount for that column to each plot
        # have to create vertical column, hehe oops
        vertColumn = []
        for column in range(0,height):
            vertColumn.append(lawn[column][row])
        highestGrass = getHighestGrass(vertColumn)
        for column in range(0,height):
            if testlawn[column][row] > highestGrass:
                testlawn[column][row] = highestGrass
    print testlawn
    print lawn

    if(testlawn == lawn):
        return "YES"
    else:
        return "NO"

inputFile = open(sys.argv[1], 'r')

outputFile = open(sys.argv[2], 'w')
outputString = ""

caseAmount = int(inputFile.readline())

lines=inputFile.readlines()

#print caseAmount

currentLine = 0

for case in range(0,caseAmount):
    lawnSize = lines[currentLine].split()

    
    lawn = [[0 for i in range(int(lawnSize[1]))] for j in range(int(lawnSize[0]))]
    for lawnRow in range(0,int(lawnSize[0])):
        lawn[lawnRow] = lines[currentLine + lawnRow+1].split()
    
    currentLine += int(lawnSize[0]) + 1
    #print case,gameBoard
    result = solveCase(lawn, int(lawnSize[1]), int(lawnSize[0]))
    print "Case #" + str(case+1) + ": " + result
    outputString = outputString + "Case #" + str(case+1) + ": " + result + "\n"

outputFile.write(outputString)


    
    