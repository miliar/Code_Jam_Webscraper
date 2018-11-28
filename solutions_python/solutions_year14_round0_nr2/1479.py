from sys import argv
from math import *

def cookieClicker(inputPath):
    inputFile = open(inputPath)
    inputList  =[w.strip() for w in inputFile.readlines()]
    caseCount = int(inputList[0])
    startIndex = 1
    for i in range(caseCount):
        l1 = inputList[i+1].split()
        C = float(l1[0])
        F = float(l1[1])
        X = float(l1[2])
        t = 0
        p = 2.0
        while True:
            if (X/p <= (C/p+X/(p+F))):
                print 'Case #'+ str(i+1)+': '+str(t+X/p) 
                break
            t += C/p 
            p += F

        


if __name__ == '__main__':
    cookieClicker(argv[1])