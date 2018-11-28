from math import *

def squareCheck(n):
    return sqrt(n).is_integer()

def revNumber(n):
    return int(str(n)[::-1])

def inputManip(filename):
    total=0
    lineIndex=1
    inFile=open(filename,"r")
    lines=inFile.readlines()
    inFile.close()
    testCases=lines[0][:-1]
    outFile=open("output1.txt", "w")
    while lineIndex<len(lines):
        startPoint=int(lines[lineIndex][:lines[lineIndex].find(' ')])
        lines[lineIndex]=lines[lineIndex][lines[lineIndex].find(' ')+1:]
        endPoint=int(lines[lineIndex])
        for i in range(startPoint, endPoint+1):
            if revNumber(i)==i and squareCheck(i):
                if revNumber(int(sqrt(i)))==int(sqrt(i)):
                    total+=1
        outFile.write("Case #%d: %d\n"%(lineIndex,total))
        lineIndex+=1
        total=0
    outFile.close()
inputManip("C-small-attempt3.in")
