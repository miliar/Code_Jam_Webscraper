import re, sys, os, math

def makeReg(word):
	word = word.replace("(", "[")
	word = word.replace(")", "]")
	return word
	
infile = open (sys.argv[1], "r")

line = infile.readline().split()
L = int(line[0])
D = int(line[1])
N = int(line[2])
words = []
for num in range(0, D):
	words.append(infile.readline().rstrip())

for num in range(0, N):
	test = infile.readline().rstrip()
	pattern = re.compile(makeReg(test))
	count = 0
	for word in words:
		if pattern.match(word) != None:
			count += 1
	print "Case #%d: %d" % (num+1, count)
infile.close()
