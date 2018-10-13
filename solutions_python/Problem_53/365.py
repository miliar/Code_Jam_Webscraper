import os
import re
import commands
import sys

def findBulbState(caseCount, nVal, kVal):
    kVal = kVal + 1
    minSwitches = pow(2,nVal)
    intFraction = kVal/minSwitches
    floatFraction = float(kVal)/float(minSwitches)
    if(float(intFraction) == floatFraction):
        print "Case #"+str(caseCount)+": ON"
    else:
        print "Case #"+str(caseCount)+": OFF"

def main():
    filename = sys.argv[1]
    try:
        inp = open(filename,'r')
    except IOError,err:
        print "ERROR:Cannot open input file:"+filename
        sys.exit(2)
    ##read input count:
    inpCount = inp.readline()
    inpCount = inpCount.strip()
    inpCount = int(inpCount)
    currCaseCount = 1
    while(currCaseCount <= inpCount):
        inputLine = inp.readline()
        inputLine = inputLine.strip()
        tempArr = re.split("\s+", inputLine)
        currNVal = int(tempArr[0])
        currKVal = int(tempArr[1])
        findBulbState(currCaseCount, currNVal, currKVal)
        currCaseCount += 1
    #end while


if __name__ == "__main__":
    main()