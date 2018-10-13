#! /usr/bin/python

def bigbro(vals):
	return sum(vals)

def lilbro(vals):
	return reduce(lambda x,y: x^y,vals)

def trans(candies, vals):
	return map(lambda x: candies[x], vals)

if __name__ == '__main__':
	import sys
	import pdb
	import itertools
	from itertools import combinations as combo
	
	f = open(sys.argv[1], 'r')
	
	test_cases = int(f.readline())
	for i in range(test_cases):
		
		N = f.readline()
		candies = map(int,f.readline().split())
	
		winner = [-1]
		candy_tries = (set(y) for x in range(1,len(candies)) for y in combo(range(len(candies)), x))
		for cset1 in candy_tries:
			cset2 = set(range(len(candies))) - cset1 # set difference
	
			real1 = trans(candies, cset1) # go from index to the candy value
			real2 = trans(candies, cset2)

			big1, big2 = bigbro(real1), bigbro(real2)
			lil1, lil2 = lilbro(real2), lilbro(real1)

			if lil1 == lil2:
				winner[0] = max(big1,big2, winner[0])

		if winner[0] == -1:
			print 'Case #%d: NO' % ((i+1))
		else:
			print 'Case #%d: %d' % ((i+1), winner[0])
	
	f.close()

