from copy import deepcopy
from collections import namedtuple
import functools
import numpy as np
import common 
from common import read_input, save_cases

def run(f):
	txt = open(f).read()
	f2 = f + '.out'
	outputs = [calculate(recipe, all_packages)
			   for recipe, all_packages in parse_input(txt)] 
	save_cases(f2, outputs)
	
def parse_input(txt):
	lines = iter([x for x in txt.split('\n') if x])
	T = int(lines.next())
	inputs = []
	for line in lines:
		N, P = line.split() 
		N, P = int(N), int(P)
		recipe = [int(x) for x in lines.next().split()]

		arr = []
		for _ in range(N):
			line = lines.next()
			arr += [sorted(int(x) for x in line.split())]
		inputs += [(recipe, arr)]
	return inputs


def agree(recipe, packages):
	assert len(recipe) == len(packages)
	bounds = 0., float("inf") 
	highs = [np.floor((p / 0.9) / r) for r, p in zip(recipe, packages)]
	lows  = [np.ceil((p / 1.1) / r)  for r, p in zip(recipe, packages)]
	if (all(x <= min(highs) for x in lows) and
		all(x >= max(lows)  for x in highs)):
		return True
	# the low ones need to be killed off
	return [i for i, x in enumerate(highs) if x < max(lows)]


def calculate(recipe, all_packages):
	def pop_front(xs):
		xs.reverse(); xs.pop(); xs.reverse()
	count = 0
	while all(all_packages):
	    packages = [p[0] for p in all_packages]
	    result = agree(recipe, packages)
	    if result == True:
	        count += 1
	        [pop_front(p) for p in all_packages]
	    else:
	        for i in result:
	            pop_front(all_packages[i])
	return count


##### 

example_input = \
"""6
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900
"""

example_output = \
"""Case #1: 1
Case #2: 0
Case #3: 1
Case #4: 0
Case #5: 3
Case #6: 3
"""

