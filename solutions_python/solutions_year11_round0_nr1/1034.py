#!/usr/bin/python

import sys

def move(current, next):
	if current < next:
		return current+1
	elif current > next:
		return current-1
	return current

def getNext(seq, start, type):
	for s in seq[start:]:
		if s[0] == type:
			return s[1]
	return 0

def solve(seq):
	nextO = getNext(seq, 0, "O")
	nextB = getNext(seq, 0, "B")
	t = 0
	O = 1
	B = 1
	for i in range(len(seq)):
		s = seq[i]	
	
		if s[0] == "O":
			while s[1] != O:
				O = move(O, nextO)
				B = move(B, nextB)
				t += 1
			#push
			nextO = getNext(seq, i+1, "O")
			B = move(B, nextB)
			t += 1
		elif s[0] == "B":
			while s[1] != B:
				O = move(O, nextO)
				B = move(B, nextB)
				t += 1
			#push
			nextB = getNext(seq, i+1, "B")
			O = move(O, nextO)
			t += 1
		
	return t

T = int(sys.stdin.readline())
lines = sys.stdin.readlines()

for t in range(T):
	parts = lines[t].split()
	N = int(parts[0])
	seq = []
	for n in range(N):
		seq.append((parts[n*2+1], int(parts[n*2+2])))
	sol = solve(seq)
	print "Case #" + str(t+1) + ": " + str(sol)

