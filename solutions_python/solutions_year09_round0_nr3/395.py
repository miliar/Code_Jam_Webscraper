import sys
import string
import os
import array

#global
lengthOfKey = 19

def FindFirst(indices, text, key):
    indices[0] = -1
    return Find(indices, text, key, 0)

def FindNext(indices, text, key):
    return Find(indices, text, key, lengthOfKey-1)
    
def Find(indices, text, key, indexToStart):
    lengthOfText = len(text)
    indexToIncrement = indexToStart
    foundOne = False
    while (indexToIncrement > -1):
        bumpBack = False
        #print "pig", indexToIncrement
        if indices[indexToIncrement] + 1 < lengthOfText:
            newIndex = text.find(key[indexToIncrement], indices[indexToIncrement]+ 1)
            #print newIndex
            if (newIndex > -1):
                indices[indexToIncrement] = newIndex
                if (indexToIncrement + 1 == lengthOfKey):
                    foundOne = True
                    #flag we are done!
                    indexToIncrement = -1
                else:
                    indexToIncrement += 1
                    if (indexToIncrement < lengthOfKey):
                        indices[indexToIncrement] = indices[indexToIncrement-1]
                    else:
                        #flag we are done
                        indexToIncrement = -1
            else:
                bumpBack = True
        else:
            bumpBack = True
                    
        if (bumpBack):
            #Then we need to go back to the previous index
            indexToIncrement -= 1
            
    return foundOne

#get input info
inputFilename = raw_input("Enter input file name:")
outputFilename = raw_input("Enter output file name:")

inputFile = open(inputFilename)
outputFile = open(outputFilename, 'w')
numberOfCases = int(inputFile.readline())
textToFind = "welcome to code jam"

#go through input
caseNumber = 0
for line in inputFile:
    caseNumber += 1
    print caseNumber
    cleanLine = line.rstrip()
    lengthOfText = len(cleanLine)
    if lengthOfText > 0:
        currentIndices = [0 for i in range(lengthOfKey)]
        found = 0
        notDone = FindFirst(currentIndices, cleanLine, textToFind)
        while (notDone):
            #print currentIndices
            found += 1
            notDone = FindNext(currentIndices, cleanLine, textToFind)
            if found > 1000000:
                found = found % 10000

        #Clean output
        found = found % 10000
        foundString = str(found)
        zeroString = "00000000"
        if len(foundString) < 4:
            foundString = zeroString[0:4-len(foundString)] + foundString
        
        #Print output      
        outputString = "Case #" + str(caseNumber) + ": "
        outputString += foundString + "\n"
        outputFile.write(outputString)

inputFile.close()
outputFile.close()
print "done"
