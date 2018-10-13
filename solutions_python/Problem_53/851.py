#! /usr/bin/env python

fin = open("inp.txt","r")

numTests = fin.readline().rstrip("\n")

for casenum,line in enumerate( fin.readlines() ):
	line = line.rstrip("\n")
	(snappers,snaps) = line.split(" ")
	bulbval = ( int(snaps) + 1 ) % (2 ** int(snappers) )
	if bulbval == 0:
		print "Case #%d: ON" % (casenum + 1)
	else:
		print "Case #%d: OFF" % (casenum + 1)
	
fin.close()