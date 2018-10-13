import os, glob, sys
import math
import string

class CombinationElement:
    def __init__(self, base1Char, base2Char, resultChar):
        self.base1Char = base1Char
        self.base2Char = base2Char
        self.resultChar = resultChar

    def checkListForCombination(self, elementList):
        endIndex = len(elementList) - 1
        if ((self.base1Char == elementList[endIndex] and self.base2Char == elementList[endIndex - 1]) or (self.base1Char == elementList[endIndex - 1] and self.base2Char == elementList[endIndex])):
            return self.resultChar

        return ""

class OpposedElement:
    def __init__(self, base1Char, base2Char):
        self.base1Char = base1Char
        self.base2Char = base2Char

    def checkListForOpposed(self, elementList):
        base1Found = False
        base2Found = False
        for element in elementList:
            if (element == self.base1Char):
                base1Found = True
            elif (element == self.base2Char):
                base2Found = True

            if base1Found and base2Found:
                return True

        return False

def processElementList(elementList, combinationElementList, opposedElementList):
    """ Don't fanny around """
    if ((len(elementList) < 2) or ((len(combinationElementList) == 0) and (len(opposedElementList) == 0))):
        return

    """ Check for combinations """
    for combinationElement in combinationElementList:
        combinationResult = combinationElement.checkListForCombination(elementList)
        if combinationResult != "":
            del elementList[len(elementList) - 1]
            del elementList[len(elementList) - 1]
            elementList.append(combinationElement.resultChar)
            break

    """ Check for opposed """
    if (len(elementList) > 1):
        for opposedElement in opposedElementList:
            if opposedElement.checkListForOpposed(elementList):
                del elementList[:]
                break;

    return
            
def playMagicka(testCaseLineInput):
    combClassList = []
    opposedClassList = []
    elementInvokeList = ""
    playInvokeList = []
    currentStringPos = 0
    caseStringList = testCaseLineInput.split()

    numberCombEls = int(caseStringList[currentStringPos])

    """ Create combination class list """
    combCount = 0
    while(combCount < numberCombEls):
        currentStringPos = currentStringPos + 1
        combClassList.append(
                   CombinationElement(caseStringList[currentStringPos][0], caseStringList[currentStringPos][1], caseStringList[currentStringPos][2]))
        combCount = combCount + 1

    currentStringPos = currentStringPos + 1
    numberOpposeEls = int(caseStringList[currentStringPos])
    """ Create opposed class list """
    opposeCount = 0
    while(opposeCount < numberOpposeEls):
        currentStringPos = currentStringPos + 1
        opposedClassList.append(OpposedElement(caseStringList[currentStringPos][0], caseStringList[currentStringPos][1]))
        opposeCount = opposeCount + 1
    
    currentStringPos = currentStringPos + 1
    if (int(caseStringList[currentStringPos]) != 0):
        currentStringPos = currentStringPos + 1
        elementInvokeList = caseStringList[currentStringPos]

    for element in elementInvokeList:
        playInvokeList.append(element)
        processElementList(playInvokeList, combClassList, opposedClassList)

    return playInvokeList
        

if __name__ == "__main__":
    f = open("B-large.in", 'r')
    out = open("B-large-attempt0.out", 'w')
    caseCount = 0

    testCaseNumberString = f.readline()
    if testCaseNumberString != "":
        testCase = f.readline()
        while (testCase != ""):
            caseCount = caseCount + 1
            out.write("Case #" + str(caseCount) + ": " + str(playMagicka(testCase)).replace("'", "") + "\n")
            testCase = f.readline()

    f.close()
    out.close()
            
