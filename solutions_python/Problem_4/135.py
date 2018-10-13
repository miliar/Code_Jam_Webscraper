from math import sqrt, pi
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(10000000)
    inFile = open('A-large.in')
    inLines = inFile.readlines()
    inFile.close()
    numCases = int(inLines[0].strip())
    index = 1
    for iCase in range(numCases):
        numOfVectors = int(inLines[index].strip())
        #print numOfVectors
        aList = inLines[index+1].strip().split(' ')
        bList = inLines[index+2].strip().split(' ')
        aList = map(int, aList)
        bList = map(int, bList)
        aList = sorted(aList)
        bList = sorted(bList)
        bList.reverse()
        #print 'a', aList
        #print 'b', bList
        minAB = 99999
        newList = []
        for i in range(len(aList)):
            newList.append(aList[i] * bList[i])
        sum = 0
        for i in range(len(newList)):
            sum += newList[i]
        # index is case definition        
        print 'Case #%d: %d' % (iCase + 1, sum)        
        ##
        index += 3