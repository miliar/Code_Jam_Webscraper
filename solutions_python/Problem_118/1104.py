import sys
import numpy as np


def isPalindrome(i):
    s = str(i)
    s2 = s[::-1]
    return s == s2
    

def solveCase(C, start, end):


    iStart = np.int(np.ceil(np.sqrt(start)))
    iEnd = np.int(np.floor(np.sqrt(end)))

    counter = 0;
    for i in np.arange(iStart, iEnd+1):
        if isPalindrome(i) and isPalindrome(i**2):
            counter += 1

    return 'Case #%i: %i' % (C, counter)



def processFile(inputFile, outputFile):
    fileIn = open(inputFile, 'rU')
    fileOut = open(outputFile, 'w')

    cases = int(fileIn.readline().strip())
    C = 0
    while C < cases:
        C += 1
        row = fileIn.readline().strip().split(' ')
        start = int(row[0])
        end = int(row[1])
        
        result = solveCase(C, start, end)
        print result
        fileOut.write(result + '\n')

    fileIn.close()
    fileOut.close()
            

processFile('C-small-attempt0.in', 'C-small-attempt0.out')
