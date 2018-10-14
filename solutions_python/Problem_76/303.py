#!/usr/bin/python

import sys

def line():
    return sys.stdin.readline()[:-1]

if __name__ == '__main__':
    numberOfCases = int(line())
    xor = lambda x,y : x^y
    for caseNumber in range(numberOfCases):
        N = int(line())
        values = map(int,line().split())

        isPossible = reduce(xor,values,0) == 0
        if isPossible:
            output = str(sum(values) - min(values)).replace('L','')
        else:
            output = 'NO'
        
        print "Case #" + str(caseNumber+1) + ": " + output
