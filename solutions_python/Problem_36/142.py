
import sys

goalstr = 'welcome to code jam'

def loadinput():
	fn = sys.argv[1]
	f = open(fn,'r')

	n = int(f.readline())
	probs = f.readlines()

	return n,probs


# Maintain counts mod n for the substrings
# When you find a new character, advance the appropriate substrings
# This could be compiled into a state machine, but don't bother for a 19 character string.
def count(str):
	counts = [0 for i in range(len(goalstr)+1)]
	counts[0] = 1		# Base case

	for c in str:
		for i in range(len(goalstr)):
			if goalstr[i] == c:
				counts[i+1] = (counts[i] + counts[i+1])%10000

	return counts[len(goalstr)]

def pad(n):
	s = str(n)
	while len(s) < 4: s = '0'+s
	return s

def solveall(n,probs):
	for i in range(n):
		c = count(probs[i])
		cs = pad(c)
		print "Case #%d: %s"%(i+1,cs)

n,probs = loadinput()
solveall(n,probs)


