# -*- coding: utf-8 -*-

import math
import itertools

def permutations(iterable, r=None):
	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	for indices in itertools.product(range(n), repeat=r):
		if len(set(indices)) == r:
			yield tuple(pool[i] for i in indices)


def parse(file):
	def str2price(number):
		d = {}
		
		d[number[0]] = 1
		if len(number)>1: 
			max = 0
			for x in number[1:]:
				if x not in d:
					d[x] = max
					max += 2 if len(d)==2 else 1
		return d
	
	lines = open(file).readlines()
	lines = [line.strip() for line in lines]
	cases = int(lines[0])
	
	not_empty = lambda x: x>0
	
	case = 0
	for i in range(1, cases*2+1, 2):
		case += 1
		number, x = lines[i].strip().split(' ')
		cams = list(map(int, lines[i+1].strip().split(' ')))
		
		result = []
		for cams_v in permutations(cams):
			r = 0
			cells = [1 for _ in range(int(number))]
			for c in cams_v:
				cells[c-1] = 0
				a = [x for x in itertools.takewhile(not_empty, cells[:c-1][::-1])]
				b = [x for x in itertools.takewhile(not_empty, cells[c:])]
				r += len(a) + len(b)
				pass
			result.append(r);
		
		print('Case #%s: %d' % (case, min(result)))
	pass

def main():
	#parse('c.in')
	parse('C-small-attempt0.in')
	

main()
