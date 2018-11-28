#!/usr/bin/python
# Zoltan Puskas <mr.zoltan.puskas@gmail.com>
# Bot Trust

import sys

fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')
testCaseNum = fin.readline()
print "Number of testcases: {}".format(testCaseNum)
currTestCase = 0

for line in fin:
	currTestCase += 1
	commands = line.rstrip().rsplit(' ')
	pressCnt = int(commands.pop(0))
	print "Number of buttons to press: {}".format(pressCnt)
	robotCommands = {}
	robotCommands['O'] = []
	robotCommands['B'] = []
	robotOrder= []
	for i in range(pressCnt):
		robotCommands[commands[i*2]].append(int(commands[i*2+1]))
		robotOrder.append(commands[i*2])
	robotStatus = {} # key-> robot, value->list[position, next button to press in the list]
	robotStatus['O'] = [1, 0]
	robotStatus['B'] = [1, 0]
	buttonsPressed = 0
	sec = 0
	while buttonsPressed < pressCnt:
		action = False
		# O robot block
		if robotStatus['O'][1] < len(robotCommands['O']):
			if robotStatus['O'][0] == robotCommands['O'][robotStatus['O'][1]]:
				if robotOrder[buttonsPressed] == 'O' and not action:
					buttonsPressed += 1
					robotStatus['O'][1] += 1
					action = True
			else:
				if robotStatus['O'][0] < robotCommands['O'][robotStatus['O'][1]]:
					robotStatus['O'][0] += 1
				if robotStatus['O'][0] > robotCommands['O'][robotStatus['O'][1]]:
					robotStatus['O'][0] -= 1

		# B robot block
		if robotStatus['B'][1] < len(robotCommands['B']):
			if robotStatus['B'][0] == robotCommands['B'][robotStatus['B'][1]]:
				if robotOrder[buttonsPressed] == 'B' and not action:
					buttonsPressed += 1
					robotStatus['B'][1] += 1
					action = True
			else:
				if robotStatus['B'][0] < robotCommands['B'][robotStatus['B'][1]]:
					robotStatus['B'][0] += 1
				if robotStatus['B'][0] > robotCommands['B'][robotStatus['B'][1]]:
					robotStatus['B'][0] -= 1
		# time
		sec += 1
	print "Time to complete: {}".format(sec)
	fout.write("Case #{}: {}\n".format(currTestCase, sec))		 

