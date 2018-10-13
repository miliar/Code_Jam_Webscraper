#!/usr/bin/python

import sys
import os

def check_winner(scan):
	wincount = 4
	if scan.count("T") == 1:
		wincount = 3
		
	if scan.count("X") >= wincount:
		return "X"
	elif scan.count("O") >= wincount:
		return "O"

	return None


nCases = int(sys.stdin.readline().strip(" \r\n"))
for case in xrange(1, nCases+1):
	unfull = True
	rows = []
	[rows.append(sys.stdin.readline().strip(" \r\n")) for _ in xrange(4)]
	
	unfull = (rows[len(rows)-1].count(".") > 0)
	
	sys.stdin.readline()
	
	#print "#Board: " + str(rows)
	
	columns = [map(lambda e : e[i], rows) for i in xrange(4)]
	
	diagonals = [[rows[i][i] for i in xrange(4)] , [rows[i][3-i] for i in xrange(4)]]
	
	results = []
	for scan in rows + columns + diagonals:
		
		#print "#Scan: " + str(scan)
		
		r = check_winner(scan)
		if r != None:
			results.append(r)
			
	if "X" in results:
		if not "O" in results:
			print "Case #%d: X won" % (case)
		else:
			print "Case #%d: Draw" % (case)
	elif "O" in results:
		print "Case #%d: O won" % (case)
	elif unfull:
		print "Case #%d: Game has not completed" % (case)
	else:
		print "Case #%d: Draw" %(case)
		
	
	
					
	
	
	
	
	
	
	
	