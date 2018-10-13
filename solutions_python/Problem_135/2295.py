import sys
import collections

input = open(sys.argv[1])
numTestCases = int(input.readline())

for t in range(1,numTestCases+1):
	lineNum1 = int(input.readline())

	arrangement1 = []
	for x in range(0,4):
		arrangement1.append(input.readline().rstrip().split(' '))

	

	lineNum2 = int(input.readline())
	arrangement2 = []
	for y in range(0,4):
		arrangement2.append(input.readline().rstrip().split(' '))

	

	combined = arrangement1[lineNum1-1] + arrangement2[lineNum2-1]

	

	duplicates = [x for x, y in collections.Counter(combined).items() if y > 1]

	output = ""
	if len(duplicates) == 0:
		output = "Volunteer cheated!"
	elif len(duplicates) == 1:
		output = str(duplicates[0])
	else:
		output = "Bad magician!"

	print "Case #"+str(t) + ":",output