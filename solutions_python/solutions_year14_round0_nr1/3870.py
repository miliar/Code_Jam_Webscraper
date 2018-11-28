#!/usr/bin/env python
#
# Google Code Jam 2014
# Qualification Round
# A - Magic Trick

import sys

def getValues(inputFile, rowNum):
    for row in range(4):
        line = inputFile.readline()[:-1]
        
        if row == rowNum:
            columns = line.split(" ")
        
    return columns

def countDuplicates(values):
    duplicates = 0
    number     = 0
    
    for value in range(4):
        for other in range(4):
            if values[0][value] == values[1][other]:
                duplicates += 1
                number = values[0][value]
                
    return duplicates, number
    
inputFile   = open(sys.argv[1], "r")
numberTests = int(inputFile.readline())
results     = []
while (numberTests > 0):
    values = []
    
    for i in range(2):
        rowNum = int(inputFile.readline()) - 1 
        values.append(getValues(inputFile, rowNum))
    
    duplicates, number = countDuplicates(values)
    
    if duplicates > 1:
        results.append("Bad magician!")
    elif duplicates == 0:
        results.append("Volunteer cheated!")
    else:
        results.append(number)
        
    numberTests -= 1

inputFile.close()
outputFile = open(sys.argv[2], "w")

for i in range(len(results)):
    outputFile.write("Case #" + str(i+1) + ": " + results[i] + "\n")