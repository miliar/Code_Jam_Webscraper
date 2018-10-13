import sys

filename = sys.argv[1]
#filename = 'test.in'

sys.stdin = open(filename,'r')
numOfCases = int(raw_input())

for x in range(1, numOfCases+1):
	candidates = []
	for z in range(0, 2):
		anwser = int(raw_input())
		for y in range(0, 4):
			if anwser == y + 1:
				candidates.append(raw_input())
			else:
				raw_input()

	firstcand = candidates[0].split()
	secondcand = candidates[1].split()
	chosen = []
	for first in firstcand:
		for second in secondcand:
			if second == first:
				chosen.append(second)	

	if len(chosen) == 0:
		print "Case #" + str(x) + ": Volunteer cheated!"
	elif len(chosen) == 1:
		print "Case #" + str(x) + ": " + chosen[0]  
	else:
		print "Case #" + str(x) + ": Bad magician!"

