
import string, os, time, sys

ordA = ord('A')

def PrintCharList(charList):
    sys.stdout.write("[")
    for i in range(0,len(charList)):
        if (i >0):
            sys.stdout.write(", ")
        print charList[i],
    sys.stdout.write("]\n")

def AddToCombineMap(combineMap, triplet):
    pair = triplet[0:2]
    altpair = pair[::-1]
    nonBase = triplet[2]
    combineMap[pair] = nonBase
    combineMap[altpair] = nonBase

def AddToDestroySet(destroySet, pair):
    x = pair[0]
    y = pair[1]
    xOrd = ord(x)-ordA
    destroySet[xOrd] = destroySet[xOrd]+y
    if (x != y):
        yOrd = ord(y)-ordA
        destroySet[yOrd] = destroySet[yOrd]+x
        
    
def HandleCase(f, caseIndex):
    caseline = f.readline().rstrip("\r\n")
    splitline = caseline.split(" ")
    
    combineMap = {}
    destroySet = []
    for i in range(0,26):
        destroySet.append("")

    numCombines = int(splitline.pop(0))
    for i in range(0, numCombines):
        AddToCombineMap(combineMap, splitline.pop(0))

    numDestroys = int(splitline.pop(0))
    for i in range(0, numDestroys):
         AddToDestroySet(destroySet, splitline.pop(0))

    numCharacters = int(splitline.pop(0))
    deck = list(splitline.pop(0))

    resultList = []
    containsLetter = []
    for i in range(0,26):
        containsLetter.append(0)

    for item in deck:
        if (len(resultList)>0):
            pair = str(resultList[-1]) + item
            if (combineMap.has_key(pair)):
                oldLetterOrd = ord(resultList[-1])-ordA
                containsLetter[oldLetterOrd] = containsLetter[oldLetterOrd]-1
                newLetter = combineMap[pair]
                newLetterOrd = ord(newLetter)-ordA
                containsLetter[newLetterOrd] = containsLetter[newLetterOrd]+1
                resultList[-1] = newLetter
                continue

            opposites = destroySet[ord(item)-ordA]
            clearList = False
            for i in range(0,len(opposites)):
                if (containsLetter[ord(opposites[i])-ordA]>0):
                    clearList = True
                    break

            if (clearList):    
                resultList = []
                for i in range(0,26):
                    containsLetter[i] = 0
                continue


        resultList.append(item)
        newLetterOrd = ord(item)-ordA;
        containsLetter[newLetterOrd] = containsLetter[newLetterOrd]+1

    result = "".join(resultList)
    header = "Case #%(count)d: " % {"count":caseIndex}
    print header,
    PrintCharList(result)


inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)

