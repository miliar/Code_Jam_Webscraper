# -*- coding: utf-8 -*-
"""
Alexander Crombie

Standing Ovation
"""

def CalculateAvailability(PeopleAtShynessLevels):
    newPeopleAtShynessLevels = []
    availablePeople = 0
    for i in range(0, len(PeopleAtShynessLevels)):
        if availablePeople < i:
            newPeopleAtShynessLevels.append(availablePeople)
        else:
            availablePeople += PeopleAtShynessLevels[i]
            newPeopleAtShynessLevels.append(availablePeople)
        
    return newPeopleAtShynessLevels


testCases = 0

testCaseList = []
numbersRequired = []

fileName = 'C:\\Users\\Asus\\Documents\\Code Jam 2015\\Qualifications\\Standing Ovation\\A-large.in'
outputFile = 'C:\\Users\\Asus\\Documents\\Code Jam 2015\\Qualifications\\Standing Ovation\\output.txt' 

with open(fileName, 'r') as inputFile:
    testCases = int(inputFile.readline())
    for line in inputFile:
        values = line.split()
        testCaseList.append([int(values[0]), values[1]])
        
        
required = []
        
for i in range(0, testCases):
    shynessLevels = list(testCaseList[i][1])    
    for j in range(0, len(shynessLevels)):
        shynessLevels[j] = int(shynessLevels[j])

    availablePeopleAtLevel = CalculateAvailability(shynessLevels)
    
#    print(availablePeopleAtLevel)
    
    peopleRequired = 0
    for j in range(0, len(shynessLevels) - 1):
        while(availablePeopleAtLevel[j] < j + 1):
            peopleRequired += 1
            shynessLevels[0] += 1
            availablePeopleAtLevel = CalculateAvailability(shynessLevels)
            
    required.append(peopleRequired)
    
with open(outputFile, 'w') as output:
    for i in range(0, len(required)):
        output.write('Case #' + str(i + 1) + ': ' + str(required[i]) + '\n')