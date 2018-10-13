

#iterates over the numbers in range A to B(A and B are string
#representations). For each number, checks the possible 'recyclings'
def FindNumRecycledInRange(A,B):
    aAsInt = int(A)
    bAsInt = int(B)
    currNo = aAsInt
    numRecycled = 0
    chosenList = []
    while currNo <= bAsInt:
        currNoAsStr = str(currNo)
        #check each possible recyling starting from just the last digit
        #currNo is n and recycledInt as m
        for lenOfBlock in range(1,len(currNoAsStr)):
            splitIndex = len(currNoAsStr)-lenOfBlock
            recycledStr = currNoAsStr[splitIndex:]+currNoAsStr[:splitIndex]
            recycledInt = int(recycledStr)
            isSatisfactory = (currNo >= aAsInt) and (recycledInt > currNo) and (recycledInt <= bAsInt) 
            if isSatisfactory:
                if (currNo,recycledInt) not in chosenList:
                    numRecycled += 1
                    chosenList.append((currNo,recycledInt))
        currNo += 1

    return numRecycled
    
def FindNumRecycled(inputFileName,outputFileName):
    inp = open(inputFileName,"r")
    out = open(outputFileName,"w")
    
    caseNo = 1

    noOfCases = int(inp.readline())

    while caseNo <= noOfCases:
        line = inp.readline()
        strippedLst = line.strip().split(" ")
        A = strippedLst[0]
        B = strippedLst[1]
        numRecycled = FindNumRecycledInRange(A,B)
        out.write("Case #"+str(caseNo)+": "+str(numRecycled)+"\n")
        caseNo += 1
    
FindNumRecycled("C-small-attempt0.in","output.txt")
