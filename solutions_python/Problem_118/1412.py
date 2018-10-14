#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rluo
#
# Created:     13/04/2013
# Copyright:   (c) rluo 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

def solve(inputfile,outputfile):
    global inFile,outFile
    inFile = file(inputfile,'r')
    outFile = open(outputfile,'w')
    totalCases = int(inFile.readline().strip())

    #do sth.
    for case in range(totalCases):
        print "Case #%d:"%(case+1),
        printout ("Case #%d:"%(case+1))
        counter = 0
        numRange = inFile.readline().strip()
        start,end = numRange.split( )
        start = int(start)
        end = int(end)
        for i in range(start,end+1):
            if isPalindrome(i) and isSquare(i):
##                print i,
                counter+=1
        printout ("%d\n"%counter)
        print ("%d"%counter)

    inFile.close()
    outFile.close()

def isPalindrome(num):
    if num<10:
        return True
    sNum = str(num)
    rNum = sNum[::-1]
    return sNum==rNum

def isSquare(num):
    root = math.sqrt(num)
    if root!=int(root):
        return False
    else:
        return isPalindrome(int(root))

def printout(s):
    outFile.write(s)

if __name__ == '__main__':
##    inputfile="C:\\dev\\q1\\debug.txt"
    inputfile="C:\\dev\\q1\\C-small-attempt0.in"
    outputfile="C:\\dev\\q1\\C-small-attempt0.out"
    solve(inputfile,outputfile)
