#!/usr/bin/python
import sys

if len(sys.argv) != 2:
	print 'Required: Filename'
	exit(2)

f = open(sys.argv[1], 'r')

def solve(totalButtons, bots, targets):
	i, timeElapsed = 0, 0
	botT, botF = 1, 1
	bonusMoveT, bonusMoveF = 0, 0


	while i < totalButtons:
		botCurrent = botT if bots[i] else botF

		bonusMoves = bonusMoveT if bots[i] else bonusMoveF
		moves = abs(targets[i] - botCurrent)
		moves = max(moves - bonusMoves, 0)

		if bots[i]:
			botT = targets[i]
		else:
			botF = targets[i]

		timeElapsed += moves + 1

		if bots[i]:
			bonusMoveT = 0
			bonusMoveF += moves + 1
		else:
			bonusMoveT += moves + 1
			bonusMoveF = 0

		i += 1

	return timeElapsed

testCasesTotal = int(f.readline())
testCaseCurrent = 1;

while testCaseCurrent <= testCasesTotal:
	input = f.readline().strip().split(' ')
	totalButtons = int(input.pop(0))
	bots, targets = list(), list()
	i = 0;
	while i < totalButtons:
		if input.pop(0) == 'O': bots.append(True)
		else: bots.append(False)
		targets.append(int(input.pop(0)))
		i += 1

	print 'Case #%d: %d' % (testCaseCurrent, solve(totalButtons, bots, targets));
	testCaseCurrent += 1;