#!/usr/bin/python

import os,sys

f = open(sys.argv[1], 'r')

def group(line):
	"""groups aaabbccc into ['aaa', 'bb', 'ccc']"""

	line = list(line)

	i = 0
	while i < len(line) -1:
		if line[i][0] == line[i+1]:
			line[i] += line[i+1]
			del line[i+1]
			i = 0
		else:
			i += 1
	return line

def test_group(line):
	assert group('aaa') == ['aaa']

def solve(s):
	m = map(group, s)
	if not reduce(lambda x, y: x if x == y else False, map(len, m)):
		return "Fegla Won"

	moves = 0
	for seq in zip(*map(group, s)):

		# all same
		if not reduce(lambda x, y: x if x == y else False, map(lambda x: x[0], seq)):
			return "Fegla Won"

		min_length = reduce(min, map(len, seq))
		max_length = reduce(max, map(len, seq))

		mtmp = []
		for l in range(min_length, max_length+1):
			mtmp.append(reduce(max, map(lambda x: x - l if x > l else l - x, map(len, seq))))

		moves += reduce(max, mtmp)
	return moves

for t in range(int(f.readline())):
	n = int(f.readline()) -1
	s = []
	for _ in range(n+1):
		s.append(f.readline().strip())

	print "Case #%d: %s" % (t+1, solve(s))
