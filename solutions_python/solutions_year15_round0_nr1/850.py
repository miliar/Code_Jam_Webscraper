#import math
#import sys
#import fractions

debug = True
inFile = "A-large.in"
outFile = inFile.rstrip(".in") + ".out"

def standingov(testNum, fin):
    dbgPrint("")
    
    dbgPrint("Test %d" % testNum)
    dbgPrint("----------")
    
    line = fin.readline().rstrip("\n")
    maxS,people = line.split(" ")
    maxS = int(maxS)
    
    dbgPrint(line)
        
    totalNumPeople = int(people[0])
    addNumPeople = 0
    
    for i in range(1, maxS+1):
        n = i - totalNumPeople
        if n > 0:
            addNumPeople += n
            totalNumPeople += n
        totalNumPeople += int(people[i])
    
    return addNumPeople

def dbgPrint(string):
    if debug:
        print(string)

def go():
    fin = open(inFile, "rU")
    fout = open(outFile, "w")
    
    numTests = int(fin.readline())
    print("Number of tests = %d" % numTests)

    for testNum in range(1,numTests+1):
        number = standingov(testNum, fin)
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
