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
        
        numTimes, numKeys, numLetters = map(int, inLines[index].strip().split(' '))
        #print numPads, numKeys, numLetters
        freqList = map(int, inLines[index + 1].strip().split(' '))
        freqList.sort()
        freqList.reverse()
        i = 1
        sum = 0
        #print len(freqList)
        #print freqList
        check = 0
        if numTimes * numKeys >= numLetters:
            while True:
                for j in range(numKeys):
                    if (numKeys * (i- 1)) + j >= len(freqList):
                        break
                    sum += freqList[(numKeys * (i - 1)) + j] * i
                    check += 1
                i += 1
                if i > numTimes:
                    break
                
            # index is case definition        
            print 'Case #%d: %d' % (iCase + 1, sum)
        else:
            print 'Case #%d: Impossible' % (iCase + 1, )       
        ##
        index += 2