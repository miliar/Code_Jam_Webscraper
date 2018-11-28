#!/usr/bin/python

import sys
from math import sqrt

def makeFile(name,top):
    f = open(name,'w')
    i = long(1)
    while i<top:
        f.write("%d\n" % (i))
        i += 1

def isFair(n):
    return n==n[::-1] 

if len(sys.argv)>=2:
    fileIn = sys.argv[1]
else:
    fileIn = 'example.txt'


with open(fileIn) as f:
    for case in range(int(f.readline())):
        (start, end) = f.readline().strip().split(' ')
        (start, end) = (int(start), int(end))

        count = long(0)
        i = long(start)
        while i <= end:
            #print "***"
            #print i
            if isFair(str(i)):
                #print "fair"
                iq = sqrt(i)
                if iq%1 == 0:
                    #print "square"
                    if isFair(str(long(sqrt(i)))):
                        #print "fairsquare"
                        count += 1
            i += 1
        
        print "Case #%d: %d" % (case+1, count)

            
        
