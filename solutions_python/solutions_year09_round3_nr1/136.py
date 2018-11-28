#!/usr/bin/python
from sys import stderr
from itertools import combinations, permutations

N=int(raw_input())

for case in range(N):
	line=raw_input()
	letters=[letter for letter in line]
	minb=len(set(letters))

	if minb==1: minb=2

	hash={}
	tally=1
	hash[letters[0]]=1
	last_assigned=1

	for letter in letters[1:]:
		tally=tally*minb
		if not letter in hash:
			if last_assigned==1:
				last_assigned=0
			elif last_assigned==0:
				last_assigned=2
			else:
				last_assigned+=1
			hash[letter]=last_assigned

		tally+=hash[letter]

	print 'Case #{0}: {1}'.format(case+1, tally)
	
	
