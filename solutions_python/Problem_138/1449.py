from sys import argv
from math import *

def dWar(inputPath):
    inputFile = open(inputPath)
    inputList  =[w.strip() for w in inputFile.readlines()]
    caseCount = int(inputList[0])
    startIndex = 1
    for i in range(caseCount):
        N = int(inputList[startIndex])
        l1 = inputList[startIndex+1].split()
        l2 = inputList[startIndex+2].split()
        for j in range(N):
            l1[j] = float(l1[j])
            l2[j] = float(l2[j])

        l1.sort()
        l1.reverse()
        l2.sort()
        l2.reverse()
        s1 = score(l1,l2,N)
        s2 = N - score(l2,l1,N)
        print 'Case #'+ str(i+1)+': '+str(s1)+' '+str(s2) 
        startIndex+=3
           
def score(l1,l2,N):
    i = 0
    s =0
    j =0
    while i < N:
        if l1[j]>l2[i]:
            s +=1
            j+=1
            i+=1
        else:
            i+=1
    return s 

        


if __name__ == '__main__':
    dWar(argv[1])