#!/bin/python
# -*- coding: utf-8 -*-


_input_file = 'C-small-attempt0.in'


from collections import deque
from math import log10
import sys
from time import clock


_max_value = 10000


_recycled = {}


def compute_all_recycled():
	for a in xrange(1, _max_value+1):
		_recycled[a] = []
		max_power = int(log10(float(a)))
		for m in xrange(1, max_power+1):
			p = pow(10,m)
			aa = (a / p) + (a % p * (pow(10,max_power+1) / p))
			if aa != a and int(log10(aa)) == int(log10(a)):
				_recycled[a].append(aa)



def proceed(lines):
	solutions = []
	i = 0
	nb_input = len(lines)

	while i < nb_input:
		nb_solutions = 0
		i = i + 1
		sys.stdout.write('Case #'+ str(i) +': ')
		sys.stdout.flush()

		line = lines.popleft().split()
		A = int(line[0])
		B = int(line[1])

		for a in xrange(A, B):
			recycled = filter(lambda b: a < b < B+1, _recycled[a])
			nb_solutions = nb_solutions + len(recycled)
		print nb_solutions



def read_input():
	inputfile = open(_input_file, 'r')
	lines = deque(filter(lambda l : l, map(lambda l : l.strip(), inputfile.read().splitlines())))
	lines.popleft()
	return lines



sys.stdout.write('Computing all recycled numbers up to '+ str(_max_value) +'... ')
sys.stdout.flush()
start = clock()
compute_all_recycled()
end = clock() - start
print 'OK (in '+ str(end - start) +'s)'


lines = read_input()
proceed(lines)

