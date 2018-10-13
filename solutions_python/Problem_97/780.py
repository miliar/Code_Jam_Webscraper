#!/usr/bin/env python

import urllib, urllib2, cookielib
import re #biblioteca que procura expressao regular
import os #roda o programa em C que trata a entrada gerada
import string
from itertools import permutations

from sys import argv
from utils import *

def perm(num):
	permlist = []
	string = str(num)
	for i in range(1, len(string)):
		# dont start with 0
		if string[i] != '0':
			permlist.append(int(string[i:] + string[:i]))
	return permlist

reader = InputReader("C-large.in", input_lines=1)
output_list = []

# number of tests
for i in reader.lines:
	# for each test
	pairs = []
	num_pairs = []
	numbers = string.split(i, ' ')
	first = int(numbers[0])
	second = int(numbers[1])
	# for each number
	for i in range(first, second + 1):
		# for each permutation
		for j in perm(i):
			if j < int(i) and j >= first and j <= second:
				num_pairs.append((j, i))
	no_repeat = set(num_pairs)
	output_list.append(len(no_repeat))
OutputWriter("output.txt", output_list)