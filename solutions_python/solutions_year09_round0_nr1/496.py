import sys
import string
import os
import array


def UpdateIndices(indices, letterPossibilities, startIndex):
    indexToIncrement = startIndex
    numberOfIndices = len(indices)
    for i in range(startIndex+1, numberOfIndices):
        indices[i] = 0
    ableToIncrement = False
    while (indexToIncrement > -1):
        if (indices[indexToIncrement] + 1 < len(letterPossibilities[indexToIncrement])):
            indices[indexToIncrement] = indices[indexToIncrement] + 1
            ableToIncrement = True
            #flag that we are done
            indexToIncrement = -1
        else:
            indices[indexToIncrement] = 0
            indexToIncrement -= 1
    
    return ableToIncrement

def FindWords(wordParts, alienDict, shortDict, longerDict, longestDict, wordLength):
    #First break up into the letters we have to choose from and the fixed letters
    numberOfWords = 0
    certainLetters = []
    firstHalfParts = []

    #DOH!  Check for initial letters before the first () grouping
    if (wordParts[0].find(")") > -1):
        certainLetters.append("")        
    
    for word in wordParts:
        if (word.find(")") < 0):
            certainLetters.append(word)
        else:
            twoHalves = word.split(")")
            firstHalfParts.append(twoHalves[0])
            if (len(twoHalves) > 1):
                certainLetters.append(twoHalves[1])
            else:
                certainLetters.append("")

    numberOfPieces = len(firstHalfParts)
    locationOfLetters = [0 for i in range(len(certainLetters[0]))]
    location = 0
    while (location < numberOfPieces):
        locationOfLetters.append(location)
        for letter in certainLetters[location+1]:
            locationOfLetters.append(location)            
        location += 1
#    if (len(locationOfLetters) != wordLength):
#        print "OMG"
#        print locationOfLetters
#        print wordLength
#        print certainLetters
#        print firstHalfParts

    #Now let's build us each word!
    pieceIndex = 0
    rangeOfIndices = [0 for i in range(numberOfPieces)]
    notDone = True
    while (notDone):
        possibleWord = "" + certainLetters[0]
        whichCertainSegment = 0
        for index in rangeOfIndices:
            whichCertainSegment += 1
            possibleWord += firstHalfParts[whichCertainSegment-1][index] + certainLetters[whichCertainSegment]
        startIndex = numberOfPieces - 1
        if (possibleWord in alienDict):
            numberOfWords += 1
        else:
            if (len(shortDict) > 0):
                if (possibleWord[0:4] not in shortDict):
                    startIndex = locationOfLetters[3]
                else:
                    if (len(longerDict) > 0):
                        if (possibleWord[0:8] not in longerDict):
                            startIndex = locationOfLetters[7]
                        else:
                            if (len(longestDict) > 0):
                                if (possibleWord[0:12] not in longestDict):
                                    startIndex = locationOfLetters[11]
                        
        notDone = UpdateIndices(rangeOfIndices, firstHalfParts, startIndex)

    #Return final string of all the good words
    return numberOfWords

#get input info
inputFilename = raw_input("Enter input file name:")
outputFilename = raw_input("Enter output file name:")

inputFile = open(inputFilename)
outputFile = open(outputFilename, 'w')
infoLine = inputFile.readline()
infoParts = infoLine.split()
lengthOfWords = int(infoParts[0])
numberOfWords = int(infoParts[1])
numberOfCases = int(infoParts[2])

#go through dictionary inputs
wordIndex = 0
alienDictionary = set()
shortDictionary = set()
longerDictionary = set()
longestDictionary = set()
useShort = False
useLonger = False
useLongest = False
if (lengthOfWords > 5):
    useShort = True
if (lengthOfWords > 9):
    useLonger = True
if (lengthOfWords > 14):
    useLongest = True
while (wordIndex < numberOfWords):
    wordIndex += 1
    wordLine = inputFile.readline()
    word = wordLine.rstrip()
    alienDictionary.add(word)
    if (useShort):
        shortDictionary.add(word[0:4])
        if (useLonger):
            longerDictionary.add(word[0:8])
            if (useLongest):
                longestDictionary.add(word[0:12])       

#go through cases
caseNumber = 0
for line in inputFile:
    if (len(line) > 1):
        caseNumber += 1
        print caseNumber
        numWords = 0
        strippedLine = line.rstrip()
        if (strippedLine.find("(") < 0):
            if (strippedLine in alienDictionary):
                numWords = 1
        else:
            lineParts = strippedLine.split("(")
            numWords = FindWords(lineParts, alienDictionary, shortDictionary, longerDictionary, longestDictionary, lengthOfWords)
              
        #Print output      
        outputString = "Case #" + str(caseNumber) + ": "
        outputString += str(numWords) + "\n"
        outputFile.write(outputString)

inputFile.close()
outputFile.close()
print "done"
