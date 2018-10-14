#!/usr/bin/env python

#https://code.google.com/codejam/contest/1460488/dashboard#s=p2

import sys

f = open(sys.argv[1])
num_tests = int(f.readline())

#print "num tests:", num_tests


def recycled(n,m):
    N = str(n)
    M = str(m)
    #print "N=", N, "M=",M
    #assert (len(M) == len(N))
    for i in range(len(N)):
        i += 1
        first = N[i:len(N)]
        last =  N[0:max(i,1)]
        #print first, ",", last
        x = '%s%s' %(first, last)
        #print "P",x
        if x == M:
            #print "MATCH:", N,M
            return True
    return False

case = 1
for line in f.readlines():
    count = 0
    (a,b) = line.split()
    A = int(a)
    B = int(b)
    # A-B, inclusive
    for x in range(B-A+1): #xxx
        n = A+x
        for y in range(B-A-x):
            m = n + y + 1
            #print "n,m",n,m
            if recycled(n,m):
                count += 1
        #print n
    #print a,b
    print "Case #%d: %d" % (case, count)
    case += 1
#for i in xrange(


#if __name__ == "__main__": 
#    print recycled(sys.argv[2], sys.argv[3])
