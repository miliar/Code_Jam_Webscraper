#!/usr/bin/env python

#open the file
import sys
myFilename= sys.argv[1]
myFile = open(myFilename, 'r')
tot = 0
#read first line
numQueries = int(myFile.readline())

for i in range(0, numQueries):
    line1 = myFile.readline()
    line2 = myFile.readline()
    info = line1.split()
    groups = line2.split()
    R = int(info[0]) #number of rides
    k = int(info[1]) #max passengers per ride
    N = int(info[2]) #num groups
    euro = 0 	     #how much the coaster earned today
    pos = 0
    for r in range(0, R):
	riders = 0
	count = 0
	while (riders + int(groups[pos%N]) <= k) and count < N:
	    count +=1
	    riders += int(groups[pos%N])
	    pos += 1
	euro += riders
    print "Case #"+str(i+1)+": "+str(euro)

