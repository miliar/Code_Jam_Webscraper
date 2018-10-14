import math
from itertools import groupby

def parseString(string):
	frequencies = []
	letters = []
	groups = ["".join(grp) for num, grp in groupby(string)]
	for group in groups:
		letters.append(group[0])
		frequencies.append(len(group))
	return letters, frequencies

def trial():
	A, B, K = [int(i) for i in raw_input().split()]
	count = 0
	for a in range(A):
		for b in range(B):
			if a & b < K:
				count += 1
	return count

T = int(raw_input())
for t in range(1,T+1):
	print "Case #%d:" % t,
	print trial()
