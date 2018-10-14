import sys
import math

def tokenize(s):
	t = []
	prev = ''
	for c in s:
		if c != prev:
			prev = c
			t.append((c, 0))
		b = t[len(t)-1]
		t[len(t)-1] = (b[0], b[1]+1)
	return t


def solve(lines, op):
	tokenized = []
	for l in lines:
		tokenized.append(tokenize(l))
	
	l = 0
	for t in tokenized:
		if l == 0:
			l = len(t)
		if l != len(t):
			return "Fegla Won"
	mint = [100 for j in range(l)]
	maxt = [0 for j in range(l)]
	char = [t[0] for t in tokenized[0]]
	for i in range(l):
		for t in tokenized:
			if t[i][0] != char[i]:
				return "Fegla Won"
			if t[i][1] < mint[i]:
				mint[i] = t[i][1]
			if t[i][1] > maxt[i]:
				maxt[i] = t[i][1]
	op = 0
	for i in range(l):
		op += maxt[i]-mint[i]

	return op


T = int(sys.stdin.readline().strip())
for t in range(T):
	#print "Problem", t+1
	n = int(sys.stdin.readline().strip())
	lines = []
	for i in range(n):
		lines.append(sys.stdin.readline().strip())
	res = solve(lines, 0)	
	
	print "Case #{0}: {1}".format(t+1, res)
