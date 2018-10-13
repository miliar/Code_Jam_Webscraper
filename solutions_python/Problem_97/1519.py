import sys
from math import sqrt

def usedPair(l, a, b):
	for i in l:
		if i[0] == a and i[1] == b:
			return True
		elif i[1] == a and i[0] == b:
			return True
	return False

def getRecycledPairs(a, b):
	pairs = []
	for i in range(a,b+1):
		for j in range(a, b+1):

			i = str(i)
			j = str(j)
			if i == j: continue
			for z in range(len(i)-1):
				new = i[len(i)-z-1:]
				new += i[:len(i)-z-1]
				if new == j and (not usedPair(pairs, i, j)):
					pairs.append((i,j))
	return len(pairs)

n = int(raw_input())
out = []

for i in range(n):
	line = raw_input()
	out.append(getRecycledPairs(int(line.split(' ')[0]), int(line.split(' ')[1])))

for i in range(n):
	sys.stdout.write("Case #" + str(i+1) + ": " + str(out[i]))
	print ''
