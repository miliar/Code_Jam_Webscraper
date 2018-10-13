import sys

numCases = int(sys.stdin.readline())

map = {}

alphabet = "abcdefghijklmnopqrstuvwxyz "
mapping  = "yhesocvxduiglbkrztnwjpfmaq "

numLetters = 27
for i in xrange(0, numLetters, 1):
	map[alphabet[i]] = mapping[i]

for i in xrange(1,numCases+1,1):
	sys.stdout.write ("Case #%d: " % i)
	line = sys.stdin.readline()
	numChars = len(line)
	for char in xrange(0, numChars, 1):
		if line[char] in map:
			sys.stdout.write(map[line[char]])
		else:
			sys.stdout.write(line[char])		
if line[numChars-1] != '\n':
	print