import glob, time, string, re, math
from math import sqrt; from itertools import count, islice
#open and read the input file

#textFile = open("out_test.txt", "w")
#sInputFileLoc = 'test.in'

#textFile = open("B-output_large.txt", "w")
#sInputFileLoc = 'B-large.in'

textFile = open("B-output_small2.txt", "w")
sInputFileLoc = 'B-small-attempt2.in'

sInputFile = open(sInputFileLoc)
sLineOutput = "Case #"
iLineRead = 0

def numListContainZero(numListZero):
    if 0 in numListZero:
        return 1
    return 0

def isTidy(numListStatus):
    L = len(numListStatus)-1
    status = False
    for x in xrange(len(numListStatus)-1):
        if numListStatus[L-1] <= numListStatus[L]:
              status = True  
        else:
            status = False
            break
        L = L - 1
    return status
        
    

def tidy_number(N):
    numList = [int(N) for N in str(N)]
    numListLen = len(numList)
    tidyNum = 0
    while 1 == 1:
        if ((numListContainZero(numList) == 1) and (numList[0] == 1)):
            tidyNum = int( '9' * (numListLen-1))
            break
        elif numListLen == 1:
            tidyNum = int(''.join(map(str, numList)))
            break
        elif  isTidy(numList) == True :
            tidyNum = int(''.join(map(str, numList)))
            break
        else:
            L = numListLen-1
            for x in xrange(numListLen - 1):
                if (numList[0] > numList[(numListLen-1)]) and (numList[(numListLen-1)] != 0):
                    numList[(numListLen-1)] = numList[(numListLen-1)] - 1
                    break
                elif (numList[L-1] > numList[L]) :
                    for y in xrange(numListLen- L):
                        numList[y+L] = 9
                    numList[L] = 9
                    numList[L-1] = (numList[L-1] - 1)
                
                L = L - 1
    return tidyNum
            

#Import the first line of the file. The first line contains how many different test cases are in the file being imported
iNumTestCases = int(sInputFile.readline())

#based on the numer of test cases in the first line, loop through these each one by one
for x in range(iNumTestCases):
    #import the first line of text
    sInputString = sInputFile.readline()
    resultsOut = tidy_number(int(sInputString))
    
    textFile.write(sLineOutput+str(x+1)+ ": " + str(resultsOut) +"\n")

textFile.close()


