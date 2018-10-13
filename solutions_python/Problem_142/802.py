#!/usr/bin/env python

def rle(s):
	last = None
	chars = []
	counts = []
	for ch in s:
		if ch == last:
			counts[len(counts) - 1] += 1
		else:
			counts.append(1)
			chars.append(ch)
			last = ch
	return chars, counts


def solve():
	N = int(raw_input())
	strings = [ raw_input() for i in range(N) ]
	reference_chars = None
	sums = None
	counts_list = []
	for chars, counts in ( rle(x) for x in strings ):
		if reference_chars == None:
			reference_chars = chars
			sums = [0]*len(counts)
		elif reference_chars != chars:
			print "Fegla Won"
			return
		for i in range(len(counts)):
			sums[i] += counts[i]
		counts_list.append(counts)
	avgs = [ int(round(float(x)/N)) for x in sums ]
	ops = 0
	for counts in counts_list:
		for i in range(len(counts)):
			ops += abs(counts[i] - avgs[i])
	print ops

T = int(raw_input())
for t in range(T):
	print "Case #%d:"%(t+1),
	solve()
