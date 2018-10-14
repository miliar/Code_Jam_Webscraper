#!/usr/bin/env python

import sys

try:
    filename = sys.argv[1]
except Exception as e:
    print str(e)
    exit()

file = open(filename)

test_cases = int(file.readline())

def solve(presses):
    orangeSequence = filter(lambda x: x[0] == 'O', presses)
    blueSequence = filter(lambda x: x[0] == 'B', presses)
    position = {}
    position['O'] = 1
    position['B'] = 1
    steps = 0
    while len(presses) > 0:
	steps += 1
	buttonPress = False
	if len(orangeSequence) > 0:
	    if position['O'] < orangeSequence[0][1]:
		position['O'] += 1
	    elif position['O'] > orangeSequence[0][1]:
		position['O'] -= 1
	    elif presses[0][0] == 'O':
		buttonPress = True
		orangeSequence = orangeSequence[1:]
	if len(blueSequence) > 0:
	    if position['B'] < blueSequence[0][1]:
		position['B'] += 1
	    elif position['B'] > blueSequence[0][1]:
		position['B'] -= 1
	    elif presses[0][0] == 'B':
		buttonPress = True
		blueSequence = blueSequence[1:]
	if buttonPress:
	    presses = presses[1:]
    return steps
	    
i = 1
for line in file:
    line = line.strip()
    fields = line.split(' ')
    pressCount = int(fields[0])
    presses = [(fields[2 * x + 1], int(fields[2 * x + 2]), x) for x in xrange(pressCount)]
    print 'Case #' + str(i) + ': ' + str(solve(presses))
    i += 1
