#!/usr/bin/python

import re

matchX = re.compile('[X|T]{4}')
matchO = re.compile('[O|T]{4}')
matchFull = re.compile('[X|O|T]{4}')

cases = raw_input()
for i in range(int(cases)):
	lines = []
	columns = []
	diags = []
	for x in range(4):
		lines.append(raw_input())

	for x in range(4):
		lines.append(''+lines[0][x]+lines[1][x]+lines[2][x]+lines[3][x])

	lines.append(''+lines[0][0]+lines[1][1]+lines[2][2]+lines[3][3])
	lines.append(''+lines[3][0]+lines[2][1]+lines[1][2]+lines[0][3])

	raw_input()

	finished = False
	for line in lines:
		if re.match(matchX, line):
			print "Case #"+str(i+1)+": X won"
			finished = True
			break
		if re.match(matchO, line):
			print "Case #"+str(i+1)+": O won"
			finished = True
			break

	if finished == False:
		for line in lines:
			if re.match(matchFull, line):
				continue
			else:
				print "Case #"+str(i+1)+": Game has not completed"
				finished = True
				break

	if finished == False:
		print "Case #"+str(i+1)+": Draw"

	
