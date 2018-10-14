# -*- coding: utf-8 -*-

import math

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
	
	for i in range(1, cases+1):
		number = lines[i].strip()
		
		d = str2price(number)
		
		base = max(len(d), 2)
		result = 0
		for j, x in list(enumerate(number[::-1])):
			result += d[x] * math.pow(base, j)
			pass
		
		#print('Case #%s:' % i, number, '->', result)
		print('Case #%s: %d' % (i, result))
	
	pass

def main():
	#parse('b.in')
	parse('A-small-attempt0.in')
	#parse('a.in')
	pass

main()
