#!/usr/bin/python

import math

def readrt(fd):
    G = fd.readline()
    g = G.split()
    r = g[0]
    t = g[1]
    return r,t

def readT(fd):
    T = fd.readline()
    return int(T)

def cpReq(r):
    newR = r+1
    a1 = r * r
    a2 = newR * newR
    a = a2 - a1
    return newR, a
    
def main(argv):
    argc = len(argv)
    if argc == 1:
        print "No input file!"
        exit(-1)
    if argc > 2:
        exit(-1)
    
    inFilename = argv[1]
    inFd = open(inFilename, "r")

    T = readT(inFd)
    #print T
    for i in range(0, T):
    #for i in range(0, 1):
        r, t = readrt(inFd)
        #print 'r,t=',r,t
        r = int(r)
        t = int(t)

        remT = t
        cntC = 0
        newR, pReq = cpReq(r)
        #print newR, pReq
        while pReq <= remT:
            cntC = cntC + 1
            remT = remT - pReq
            #print remT
            newR, pReq = cpReq(newR+1)
            #print newR, pReq

        print 'Case #'+str(i+1)+':',
        print cntC
            
    inFd.close()
    exit(0)


if __name__ == "__main__":
    import sys
    main(sys.argv)



    

