#! /usr/bin/env python

from collections import deque

fname = 'A-small-attempt1'
fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def breakchunks(s):
	chunks = []
	lastchunk = None
	prevx = None
	for x in s:
		if x == prevx:
			lastchunk.append(x)
		else:
			lastchunk = [x]
			chunks.append(lastchunk)
		prevx = x
	return chunks

def solve(fin):
	N = int(fin.readline())
	words = []
	for i in range(N):
		words.append(breakchunks(fin.readline().strip()))
	moves = 0
	length = len(words[0])
	for w in words:
		if length != len(w):
			return "Fegla Won"
	for chunks in zip(*words):
		lengths = map(len, chunks)
		char = chunks[0][0]
		avg = round(1. * sum(lengths) / len(lengths))
		for c in chunks:
			if char != c[0]:
				return "Fegla Won"
		for l in lengths:
			moves += abs(l - avg)
	return int(moves)

T = int(fin.readline())
for i in xrange(1,T+1):
	fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
