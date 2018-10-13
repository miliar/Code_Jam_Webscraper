#!/usr/bin/python

import math

def readLimits(fd):
    G = fd.readline()
    r = G.split()
    ll = int(r[0])
    ul = int(r[1])
    return ll, ul

def readT(fd):
    T = fd.readline()
    return int(T)

def isPalindrome(p):
    pStr = str(p)
    l = len(pStr)
    for i in range(0, l/2):
        #print p, l, i, i+1
        if pStr[i:i+1] != pStr[l-i-1:l-i]:
            #print 'chars = '+pStr[i:i+1], pStr[l-i-1: l-1]
            return False
    return True

def computeSqrt(i):
    iSqrt = int(math.sqrt(i))
    return iSqrt

def computeSq(i):
    iSq = i * i
    return iSq

def isWithinLimits(ll, ul, i):
    if ll <= i and i <= ul:
        return True
    else:
        return False

def main(argv):
    argc = len(argv)
    if argc == 1:
        print 'No input file!'
        exit(-1)
    if argc > 2:
        exit(-1)
    
    inFilename = argv[1]
    inFd = open(inFilename, "r")

    T = readT(inFd)

    for i in range(0, T):
        ll, ul = readLimits(inFd)
        #print ll, ul

        c = 0

        sll = int(math.sqrt(ll))
        sul = int(math.sqrt(ul))+1

        for j in range(sll, sul):
            if isPalindrome(j):
                jSq = computeSq(j)
                #print 'jSq='+str(jSq)
                if jSq >= ll and jSq <= ul:
                    if isPalindrome(jSq):
                        c = c + 1

        print 'Case #'+str(i+1)+':',
        print c

    inFd.close()
    exit(0)


if __name__ == "__main__":
    import sys
    main(sys.argv)



    

