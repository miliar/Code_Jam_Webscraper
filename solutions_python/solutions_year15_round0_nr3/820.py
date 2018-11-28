# /user/bin/python
__author__ = 'Pilar Gomez Moya'

import math
# In order to process negative numbers, we are going to use integers the following way:
# 1 = 1
# i = 2
# j = 3
# k = 4
dict1 = {1: 1, 2: 2, 3: 3, 4: 4}
dicti = {1: 2, 2: -1, 3: 4, 4: -3}
dictj = {1: 3, 2: -4, 3: -1, 4: 2}
dictk = {1: 4, 2: 3, 3: -2, 4: -1}

productMatrix = {1: dict1, 2: dicti, 3: dictj, 4: dictk}

translationDictionary = {'1': 1, 'i': 2, 'j': 3, 'k': 4}


def parseInput(fileName, listOfInputs):
    #read raw input from the file
    fo = open(fileName, "r+")
    rawInput = fo.readlines()
    #read the first item that will indicate
    #the number of cases and discard it
    numCases = int(rawInput.pop(0))

    #TODO integrity check: assert the length of rawInput is numCases+1
    #Process each line (each case)
    for x in range(0, numCases):
        #at the end, what I want, is the whole string already built
        sizesString = rawInput[2 * x]
        mySubString = rawInput[(2 * x) + 1].rstrip('\n')
        #2 sizes: first the size of the substring and then the number of repetitions
        sizes = [int(i) for i in sizesString.split(' ')]
        stringsList = []
        for i in range(0, sizes[1]):
            stringsList.append(mySubString)
        listOfInputs.append(translateStringToIntegers(''.join(stringsList)))
    fo.close()


def translateStringToIntegers(longString):
    listOfIntegers = []
    for char in longString:
        listOfIntegers.append(translationDictionary[char])
    return listOfIntegers


def findMatchingSubstrings(target, integersList, processOnlyOne, listOfSubstrings):
    if target < -4 & target > 4:
        return 0
    processingList = integersList
    for x in range(0, len(integersList) - 1):
        currentSolution = processingList[1:len(processingList)]
        if processingList[0] == target:
            listOfSubstrings.append(currentSolution)
            if(processOnlyOne):
                break
        tempList = []
        product = int(productMatrix[math.fabs(processingList[0])][math.fabs(processingList[1])])
        if processingList[0] < 0:
            product = product * -1
        if processingList[1] < 0:
            product = product * -1

        tempList.append(product)
        processingList[0:2]= tempList
    if processingList[0] == target:
        emptyList = []
        listOfSubstrings.append(emptyList)


myListOfInputs =[]
parseInput("input.txt", myListOfInputs)
outputFile = open("output.txt", "w+")
numInput = 1
for badStringIntRepresentation in myListOfInputs:
    substringsToMatchJList = []
    solutionFound = False
    findMatchingSubstrings(2, badStringIntRepresentation, True, substringsToMatchJList)
    if len(substringsToMatchJList)> 0:
        substringsToMatchKList = []
        findMatchingSubstrings(3,substringsToMatchJList[0],True, substringsToMatchKList)
        if len(substringsToMatchKList)> 0:
            leftOvers = []
            findMatchingSubstrings(4,substringsToMatchKList[0],False, leftOvers)
            if len(leftOvers)> 0:
                if leftOvers[len(leftOvers)-1] == []:
                    solutionFound = True

    if solutionFound:
        print "Case #%d: YES"%(numInput )
        outputFile.write("Case #%d: YES\n"%(numInput ))
    else:
        print "Case #%d: NO"%(numInput )
        outputFile.write("Case #%d: NO\n"%(numInput ))
    numInput+=1