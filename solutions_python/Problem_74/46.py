#!/usr/bin/python
import sys


infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())
caseNum = 0

for case in range(numCases):
	caseNum += 1
	line = infile.readline().split()
	numButtons = int(line[0])
	
	buttons = []
	
	for i in range(numButtons):
		buttons.append((int(line[2*i+1] == 'B'), int(line[2*i+2])))
	
	pos = [1,1]
	count = 0
	
	while buttons:
		count += 1
		
		#print "--- ", pos
		
		nextPlayer = buttons[0][0]
		diff = buttons[0][1] - pos[nextPlayer]
		if diff == 0:
			buttons.pop(0)
		else:
			pos[nextPlayer] += diff / abs(diff)
			
		otherPlayer = int(not nextPlayer)
		for button in buttons:
			if button[0] == otherPlayer:
				diff = button[1] - pos[otherPlayer]
				if diff != 0:
					pos[otherPlayer] += diff / abs(diff)
				break
				
	print "Case #%s: %s" % (caseNum, count)
