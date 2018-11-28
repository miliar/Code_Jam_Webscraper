#!/usr/bin/python
# warning slow
import os, sys

def getCharIndex(char):
	ref = 'a'
	return ord(char) - ord('a')
def translateLine(line):
	str = ''
	for i in range(len(line)):
		if line[i] == ' ':
			str += ' '
		else:
			str += chr(coded.index(line[i]) + ref)
	return str		

coded = ['y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q']


ref = ord('a')
infile = sys.argv[1]
filelines = open(infile, 'r').readlines()
infileLength = int(filelines[0].rstrip('\n'))
writefile = open(sys.argv[0]+'.out', 'w')
for i in range(infileLength):
	writefile.write("Case #%d: %s\n" % (i+1, translateLine(filelines[i+1].rstrip('\n'))))
	


	