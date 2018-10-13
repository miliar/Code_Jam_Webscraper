import time
#import math
#import sys
#import fractions

debug = False
inFile = "A-large.in"
outFile = inFile.rstrip(".in") + ".out"

def mushmonst(testNum, fin):
    dbgPrint("")
    
    dbgPrint("Test %d" % testNum)
    dbgPrint("----------")
    
    numIntv = fin.readline().rstrip("\n")
    dbgPrint(numIntv)
    numIntv = int(numIntv)
    
    mushCounts = fin.readline().rstrip("\n").split(" ")
    dbgPrint(mushCounts)
    
    meth1Count = 0
    curCount = int(mushCounts[0])
    maxDiff = 0
    for i in range(1, len(mushCounts)):
        nextCount = int(mushCounts[i])
        #dbgPrint("%d  -  %d" % (curCount, nextCount))
        diff = curCount - nextCount
        if nextCount < curCount:
            meth1Count += diff
        if maxDiff < diff:
            maxDiff = diff
        curCount = nextCount
        #dbgPrint(meth1Count)
    
    dbgPrint(maxDiff)
    
    meth2Count = 0
    for i in range(len(mushCounts)-1):
        c = int(mushCounts[i])
        meth2Count += (maxDiff if c >= maxDiff else c)
        #dbgPrint(meth2Count)
    
    return (meth1Count, meth2Count)

def dbgPrint(string):
    if debug:
        print(string)

def go():
    fin = open(inFile, "rU")
    fout = open(outFile, "w")
    
    numTests = int(fin.readline())
    print("Number of tests = %d" % numTests)
    
    programStartTime = time.clock()
    
    for testNum in range(1,numTests+1):
        caseStartTime = time.clock()
        
        n1, n2 = mushmonst(testNum, fin)
        outStr = "Case #%d: %s %s" % (testNum, n1, n2)
        print("%s" % outStr)
        fout.write("%s\n" % outStr)
        
        caseEndTime = time.clock()
        dbgPrint("time = %s" % (caseEndTime - caseStartTime))
    
    programEndTime = time.clock()
    dbgPrint("Total time = %s" % (programEndTime - programStartTime))
    
    fout.close()
    fin.close()

if __name__ == "__main__":
    go()
