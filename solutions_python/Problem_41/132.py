import sys
import string
import os
import array

def BumpUpBigOne(numString, currentIndex):
    #currentIndex is the one we are replacing
    #Find the next smallest digit greater than the one we are replacing
    #Get that index
    digitToReplace = int(numString[currentIndex])
    replacerIndex = currentIndex + 1
    replacerDigit = int(numString[replacerIndex])
    index = currentIndex + 1
    while (index < len(numString)):
        currentDigit = int(numString[index])
        if (currentDigit > digitToReplace and currentDigit < replacerDigit):
            replacerIndex = index
            replacerDigit = int(numString[replacerIndex])
        index += 1

    #Ok, got the index to replace with the one we are replacing
    firstString = numString[0:currentIndex] + str(replacerDigit)
    secondStringBits = numString[currentIndex:replacerIndex] + numString[replacerIndex+1:]
    secondStringList = sorted(secondStringBits)
    secondStringCrap = ""
    secondString = secondStringCrap.join(secondStringList)
    return firstString + secondString

def AddZeroAndReOrder(numString):
    #count num zeros
    #get sorted string
    #remove leading zeros
    #insert num zeroes + 1 after first
    #return
    numZeroes = numString.count("0")
    sortedString = ""
    sortedString = sortedString.join(sorted(numString))
    newString = sortedString[numZeroes:]
    for i in range(numZeroes+1):
        newString = newString[0] + "0" + newString[1:]
    return newString

def AllSameDigits(currentNumber):
    numString = currentNumber
    firstDigit = numString[0]
    allSame = True
    for digit in numString:
        if (firstDigit != digit):
            allSame = False
            break
    return allSame

def TimeToBumpUpBigOne(numString):
    currentIndex = len(numString) - 1
    #Find first decrease from the right if any
    lastDigit = int(numString[currentIndex])
    foundDrop = False
    while (currentIndex > -1):
        thisDigit = int(numString[currentIndex])
        if (thisDigit < lastDigit):
            foundDrop = True
            break
        lastDigit = thisDigit
        currentIndex -= 1

    nextNum = ""
    if (foundDrop):
        nextNum = BumpUpBigOne(numString, currentIndex)
    else:
        nextNum = AddZeroAndReOrder(numString)
    return nextNum
        

def SwapLastTwoDistinctDigits(numString):
    currentIndex = len(numString) - 1
    lastDigit = int(numString[currentIndex])
    while (lastDigit == int(numString[currentIndex])):
        currentIndex -= 1
    #now ot put the new string together
    nextNumberString = numString[0:currentIndex] + str(lastDigit) + numString[currentIndex:-1]
    return nextNumberString

def FindNext(currentNumber):
    numString = str(currentNumber)
    #Find last increasing set index
    startOfIncreasingSet = 0
    currentIndex = 1
    lastDigit = int(numString[0])
    while (currentIndex < len(numString)):
        nextDigit = int(numString[currentIndex])
        if (lastDigit > nextDigit):
            startOfIncreasingSet = currentIndex
        lastDigit = nextDigit
        currentIndex +=1
        
    #now analyze
    #print "Number is ", numString
    #print "Increasing start is ", startOfIncreasingSet
    nextNumber = numString[startOfIncreasingSet:]
    if (len(nextNumber) > 1 and AllSameDigits(nextNumber)):
        nextNumber = TimeToBumpUpBigOne(numString)
    elif (startOfIncreasingSet < len(numString) - 1):
        nextNumber = SwapLastTwoDistinctDigits(numString)
    else:
        nextNumber = TimeToBumpUpBigOne(numString)
    return nextNumber

#get input info
inputFilename = raw_input("Enter input file name:")
outputFilename = raw_input("Enter output file name:")

inputFile = open(inputFilename)
outputFile = open(outputFilename, 'w')
numberOfCases = int(inputFile.readline())

#go through input
caseNumber = 0
for line in inputFile:
    caseNumber += 1
    print caseNumber
    currentN = int(line)
    nextNum = ""
    if (currentN > 0 and currentN < 10):
        nextNum = str(currentN * 10)
    elif (currentN > 0 and AllSameDigits(str(currentN))):
        nextNum = TimeToBumpUpBigOne(str(currentN))
    elif currentN > 0:
        nextNum = FindNext(currentN)
    if currentN > 0:
        #Print output
        #print nextNum
        outputString = "Case #" + str(caseNumber) + ": "
        outputString += nextNum + "\n"
        outputFile.write(outputString)

inputFile.close()
outputFile.close()
print "done"
