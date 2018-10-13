#!/bin/python
# -*- coding: utf-8 -*-


_input_file = 'B-large.in'


from collections import deque
from math import log10
import sys
from time import clock


_triplets = {}


def compute_all_triplets():
	for s in xrange(0, 31):
		_triplets[s] = []
	for a,b,c in xrange(0,11):
		for b in xrange(a,11):
			for c in xrange(b,11):
				_triplets[a+b+c].append((a,b,c))


def proceed(lines):
	solutions = []
	i = 0
	nb_input = len(lines)

	while i < nb_input:
		nb_solutions = 0
		i = i + 1
		sys.stdout.write('Case #'+ str(i) +': ')
		sys.stdout.flush()

		line = map(lambda s : int(s), lines.popleft().split())
		S = int(line[1])
		p = int(line[2])
		triplets = filter(lambda s : s > max(3*p - 5, p-1), line[3:])
		safes = filter(lambda s : s > max(3*p - 3, p-1), triplets)
		print len(safes) + min(S, len(triplets) - len(safes))#, "-", S, p, line[3:], safes


def read_input():
	inputfile = open(_input_file, 'r')
	lines = deque(filter(lambda l : l, map(lambda l : l.strip(), inputfile.read().splitlines())))
	lines.popleft()
	return lines

lines = read_input()
proceed(lines)

