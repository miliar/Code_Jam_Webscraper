from sys import argv
from math import *

def magicTrick(inputPath):
    inputFile = open(inputPath)
    inputList  =[w.strip() for w in inputFile.readlines()]
    caseCount = int(inputList[0])
    startIndex = 1
    for i in range(caseCount):
        t1 = set(inputList[startIndex+int(inputList[startIndex])].split())
        startIndex += 5
        t2 = set(inputList[startIndex+int(inputList[startIndex])].split())
        
        hitCount = len(t1&t2)
        if hitCount ==1:
            print 'Case #'+ str(i+1)+': '+(t1&t2).pop()
        elif hitCount >1:
            print 'Case #'+ str(i+1)+': Bad magician!'
        else:
            print 'Case #'+ str(i+1)+': Volunteer cheated!'
        startIndex +=5


if __name__ == '__main__':
    magicTrick(argv[1])