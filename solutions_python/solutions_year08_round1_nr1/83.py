#!/usr/bin/python

import sys

def getline(infile):
    return infile.readline().strip()

def getint(infile):
    return int(getline(infile))

if __name__ == '__main__':
    infile = open(sys.argv[1])
    #loop for each test case
    for i in range(getint(infile)):
        getline(infile)
        v1 = [int(x) for x in getline(infile).split()]
        v1.sort()
        v2 = [int(x) for x in getline(infile).split()]
        v2.sort()
        v2.reverse()

        product = 0
        for x, y in zip(v1,v2):
            product += x*y

        print "Case", "#"+str(i+1)+":", product
