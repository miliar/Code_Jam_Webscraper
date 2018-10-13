#!/usr/bin/python

import sys

def deficit(str):
	result = 0
	preceding = 0

	for i in range(len(str)):
		result = max(result, i-preceding)
		preceding += int(str[i])

	return result

if __name__ == "__main__":
	sys.stdin.readline()
	for i,line in enumerate(sys.stdin.readlines()):
		maxShy, levels = line.strip().split()
		print "Case #{0}: {1}".format(str(i+1), str(deficit(levels)))
