#!/usr/bin/env python

import sys

def solve(n, cmd):
	prevO = 1
	prevB = 1
	prevR = cmd[0]
	prevSteps = 0
	timeTotal = 0
	for i in range(n):
		r = cmd[i*2]
		b = int(cmd[i*2+1])
		if r == 'O':
			if prevR == 'O':
				timeTotal += abs(prevO - b) + 1
				prevSteps += abs(prevO - b) + 1
			else:
				diff = abs(prevO - b) - prevSteps
				if diff > 0:
					timeTotal += diff + 1
					prevSteps  = diff + 1
				else:
					timeTotal += 1
					prevSteps  = 1
			prevO = b
			prevR = 'O'
		if r == 'B':
			if prevR == 'B':
				timeTotal += abs(prevB - b) + 1
				prevSteps += abs(prevB - b) + 1
			else:
				diff = abs(prevB - b) - prevSteps
				if diff > 0:
					timeTotal += diff + 1
					prevSteps  = diff + 1
				else:
					timeTotal += 1
					prevSteps  = 1
			prevB = b
			prevR = 'B'
	
	return timeTotal

def main(infile):
	n = int(infile.readline())
	for i in range(n):
		cmd = infile.readline().split()
		m = int(cmd.pop(0))
		print 'Case #%s: %s' % (i+1, solve(m, cmd))

main(sys.stdin)
