#!/usr/bin/env python

import sys

def processFile(fileName):
	cases = []
	with open(fileName) as f:
		line = f.readline()
		while (line):
			case = line.split()
			if (len(case) > 1):
				cases.append(case[1])
			line = f.readline()
	return cases


def main():
	fileName = sys.argv[1]
	cases = processFile(fileName)
	#print(cases)

	for i in range(0, len(cases)):
		case = cases[i]
		stands = list(case)
		currentStand = 0
		toInvite = 0
		for j in range(0, len(stands)):
			deficit = j - currentStand
			if deficit > 0:
				toInvite += deficit
				currentStand += deficit
			currentStand += int(stands[j])
		print("Case #%s: %s" % (i+1, toInvite))


if __name__=='__main__':
	main()
