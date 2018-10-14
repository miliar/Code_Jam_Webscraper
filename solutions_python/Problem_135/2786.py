#!/usr/bin/python
import sys

if len(sys.argv) != 2:
	print sys.argv[0], '<input file>'
	sys.exit(1)

fin = open(sys.argv[1], 'r')

cases = int(fin.readline().strip())

for i in range(0, cases):
	print 'Case #' + `i+1` + ':',
	firstShuffle = [ None, None, None, None]

	firstTry = int(fin.readline().strip())
	firstShuffle[0] = fin.readline().strip().split(' ')
	firstShuffle[1] = fin.readline().strip().split(' ')
	firstShuffle[2] = fin.readline().strip().split(' ')
	firstShuffle[3] = fin.readline().strip().split(' ')

	secondShuffle = [ None, None, None, None]

	secondTry = int(fin.readline().strip())
	secondShuffle[0] = fin.readline().strip().split(' ')
	secondShuffle[1] = fin.readline().strip().split(' ')
	secondShuffle[2] = fin.readline().strip().split(' ')
	secondShuffle[3] = fin.readline().strip().split(' ')

	firstGroup = firstShuffle[firstTry - 1]
	secondGroup = secondShuffle[secondTry - 1]

	matches = set(firstGroup).intersection(set(secondGroup))

	if len(matches) == 1:
		print matches.pop()
	elif len(matches) > 1:
		print 'Bad magician!'
	else:
		print 'Volunteer cheated!'
