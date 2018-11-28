import math
#import sys
#import fractions

debug = True
inFile = "B-small-attempt2.in"
outFile = inFile.rstrip(".in") + ".out"

def determineSplits(max, numMax, steps, prevAdjMax):
    adjMax = max/(steps+1.0) + (steps*numMax)
    #dbgPrint("max = %d  -  numMax = %d  -  steps = %d  -  adjMax = %f  -  prevAdjMax = %f" % (max,numMax,steps,adjMax,prevAdjMax))
    if adjMax < prevAdjMax:
        return determineSplits(max, numMax, steps+1, adjMax)
    else:
        return steps-1

def infhousepan(testNum, fin):
    dbgPrint("")
    
    dbgPrint("Test %d" % testNum)
    dbgPrint("----------")
    
    startDiners = fin.readline().rstrip("\n")
    dbgPrint(startDiners)
    
    line = fin.readline().rstrip("\n")
    tmpPlates = line.split(" ")
    dbgPrint(tmpPlates)
    
    platesDict = {}
    for i in range(len(tmpPlates)):
        n = int(tmpPlates[i])
        if n in platesDict:
            platesDict[n] += 1
        else:
            platesDict[n] = 1
    
    dbgPrint(platesDict)
    
    bkpPlatesDict = platesDict.copy()
    
    maxPancakes = sorted(platesDict.keys())[-1]
    originalMax = maxPancakes
    
    minMinSeen = maxPancakes
    
    numPasses = 1
    if 9 in platesDict:
        numPasses = 2
    
    for p in range(numPasses):
        #dbgPrint("pass #%d" % (p))
        numMinToFinish = 0
    
        platesDict = bkpPlatesDict.copy()
    
        maxPancakes = sorted(platesDict.keys())[-1]

        checkSplit = (maxPancakes > 1)
        while checkSplit:
            if maxPancakes == 9:
                steps = p+1
            else:
                steps = determineSplits(maxPancakes, platesDict[maxPancakes], 1, maxPancakes)
                if steps > 1:
                    steps = 1
            #dbgPrint("split %d across %d steps" % (maxPancakes,steps))
        
            nextMaxPancakes = 0 if len(platesDict) == 1 else sorted(platesDict.keys())[-2]
            
            if steps == 0:
                break
        
            splits = []
            max = maxPancakes
            for s in range(steps):
                dbgPrint(max)
                dbgPrint(steps+1-s)
                n = int(math.ceil(max / (steps+1.0-s)))
                splits.append(n)
                max -= n
            splits.append(max)
            dbgPrint(splits)
            
            numMinToFinish += (steps*platesDict[maxPancakes])
            
            for s in range(len(splits)):
                platesDict[splits[s]] = platesDict.get(splits[s], 0) + platesDict[maxPancakes]
            
            platesDict.pop(maxPancakes)
            maxPancakes = sorted(platesDict.keys())[-1]
            dbgPrint("numMinToFinish = %d  -  maxPancakes = %d  -  minMinSeen = %d" % (numMinToFinish,maxPancakes,minMinSeen))
            if numMinToFinish + maxPancakes < minMinSeen:
                minMinSeen = numMinToFinish + maxPancakes
    
    dbgPrint("numMinToFinish = %d  -  maxPancakes = %d  -  minMinSeen = %d" % (numMinToFinish,maxPancakes,minMinSeen))

    numMinToFinish = minMinSeen
    
    dbgPrint(numMinToFinish)
    dbgPrint(platesDict)
    
    if numMinToFinish > originalMax:
        numMinToFinish = originalMax
    
    return numMinToFinish

def dbgPrint(string):
    if debug:
        print(string)

def go():
    fin = open(inFile, "rU")
    fout = open(outFile, "w")
    
    numTests = int(fin.readline())
    print("Number of tests = %d" % numTests)

    for testNum in range(1,numTests+1):
        number = infhousepan(testNum, fin)
        if number < 0:
            outStr = "Case #%d: impossible" % (testNum)
        else:
            outStr = "Case #%d: %s" % (testNum, number)
        print("%s" % outStr)
        fout.write("%s\n" % outStr)

    fout.close()
    fin.close()

if __name__ == "__main__":
    go()
