#import sys
#import numpy as np
#import random as rnd
#from math import log, pi
BIGNUM = 1000000007
factTab = [1 for i in xrange(200)]
for i in xrange(1,200):
	factTab[i] = factTab[i-1]*i;
	factTab[i] %= BIGNUM;

def solve_case(S):
	global factTab
	global BIGNUM
	#First, look for middle characters distinct from start and end characters
	mids = [False for i in range(26)]
	for s in S:
		curmids = [False for i in range(26)]
		cmlist = []
		if s[0]==s[-1]:
			# start and end the same: all characters must be the same
			if len(set(s))>1:
				return 0
		else:# start and end different, any OTHER characters must occur in runs
			if len(s)>2:
				prevch = s[0]
				done = False
				for ch in s[1:-1]:
					nch = ord(ch)-ord('a')
					if done:				# 'end' character has already come up
						if ch!=s[-1]:		# so if it isn't the end character now
							return 0		# then we have an isolated end character which will not do
					else:
						if ch==s[-1]:			# First time we see the end character
							done = True		# so we must ensure the rest of the characters are end-characters
						else:
							if ch != prevch:						# New run...
								if (ch==s[0]) or (curmids[nch]) or (mids[nch]):	
									return 0	# If it has already occurred as a run in this or other strings in the middle, we have two groups and the game's up
								curmids[nch] = True
								cmlist.append(nch)
					prevch = ch
				for nc in cmlist:
					mids[nc] = True
	
	for s in S:
		if (mids[ord(s[0])-ord('a')]) or (mids[ord(s[-1])-ord('a')]):
			return 0
	
	se = []
	reps = [0 for i in xrange(26)]
	starts = [i for i in xrange(26)]
	ends = [i for i in xrange(26)]
	for s in S:
		a, b = ord(s[0])-ord('a'), ord(s[-1])-ord('a')
		se.append((a,b))
		if(a == b):
			reps[a]+=1
		else:
			if starts[a]!=a:
				return 0 # two equal starts with different ends
			else:
				starts[a] = b
			if ends[b]!=b:
				return 0 # two equal ends with different starts
			else:
				ends[b] = a
	
	units = []
	for i in xrange(26):
		if ends[i]==i and (reps[i]>0 or starts[i]!=i): # a unit can start here
			cur = i 
			nr = factTab[reps[cur]]
			while(starts[cur]!=cur):
				cur = starts[cur]
				nr *= factTab[reps[cur]]
				nr %= BIGNUM
			units.append(nr)
			
	if len(units)==0:
		return 0
	
	final = factTab[len(units)]
	for u in units:
		final*=u
		final%=BIGNUM
	
	
	return final

def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [x.strip().split() for x in fin.readlines()]
	fin.close()
	
	res = []
	for casenr in xrange(1, int(L[0][0])+1):
		sol = solve_case(L[2*casenr])
		res.append('Case #' + str(casenr) + ': ' + str(sol) + '\n')
	
	fout = open(out_name, 'w')
	fout.writelines(res)
	fout.close()
	return


#sys.setrecursionlimit(1010)	
#solve('B-test.in', 'B-test.out')
#solve('B-small-attempt3.in', 'B-small-attempt3.out')
solve('B-large.in', 'B-large.out')
