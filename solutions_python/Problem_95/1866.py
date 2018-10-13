#!/usr/bin/python
import sys
cmap = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z', 'z':'q'}

inFile = file(sys.argv[1])

N = None
caseNum = 0
for line in inFile:
	if N == None:
		N = int(line[:-1])
	else:
		caseNum += 1
		outLine = "Case #%d: " % caseNum
		for c in line[:-1]:
			outLine += cmap[c]
		print outLine
	if caseNum >= N:
		break
		
		
