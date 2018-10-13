#!/usr/bin/python2
import sys
import numpy as np

def isSquare(v):
    sq = np.floor(np.sqrt(v))
    if v == np.square(sq):
        return int(sq)
    else :
        return 0

def isPal(v):
    vs = str(v)
    return vs == vs[::-1]

def getPal(m, n):
    count = 0
    for i in np.arange(m, n+1):
        sq = isSquare(i)
        if sq != 0 :
            if isPal(sq) and isPal(i) :
                count = count + 1
    return count

def readParams(inputFile):

    f = open(inputFile)
    lines = [ e.strip() for e in f.readlines()]
    f.close()

    test_cases = int(lines[0])

    case = 1
    for line in lines[1:] :

        if case > test_cases:
            return

        m, n = tuple([ int(e) for e in line.split() ])

        print "Case #%s: %s"%(case,getPal(m, n))

        case = case + 1


if __name__ == "__main__" :

    if( len(sys.argv) < 2 ) :
        readParams("tc")
    else :
        readParams(sys.argv[1])
