#!/usr/bin/env python

#open the file
import sys
myFilename= sys.argv[1]
myFile = open(myFilename, 'r')
num = 0
for line in myFile:
   r = line.split()
   if (len(r) >1):
	if (int(r[1])%2**int(r[0])==2**int(r[0])-1):
	    print "Case #"+str(num)+": ON"
	else:
	    print "Case #"+str(num)+": OFF"
   num += 1
	    
