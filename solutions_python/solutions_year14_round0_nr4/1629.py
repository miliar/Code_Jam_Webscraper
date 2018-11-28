#!/usr/local/bin/python

def readlist(fn): return map(fn,raw_input().split())
def read(fn): return fn(raw_input())

def find_heavier_block(L,b):
	lo,hi = 0,len(L)-1
	while lo<hi:
		mid = lo + (hi-lo)/2
		if L[mid]>b: hi=mid
		else: lo=mid+1
	if lo >= len(L) or L[lo]<=b: return None
	return lo

class Case:

	def run(self):
		n = read(int)
		N = sorted(readlist(float))
		K = sorted(readlist(float))
	
		# normal war
		Kc = K[:]
		score_war = n
		for n in N:
			k_choice = find_heavier_block(Kc,n)
			if k_choice is not None:
				score_war -= 1
				del Kc[k_choice]

		# deceitful war
		Nc = N[:]
		score_war_d = 0
		for k in K:
			n_choice = find_heavier_block(Nc,k)
			if n_choice is not None:
				score_war_d += 1
				del Nc[n_choice]

		self.sol = [score_war_d,score_war]

	def __str__(self):
		return "Case #%d: %s" % (self.caseno,' '.join(map(str,self.sol)))

	def __init__(self,caseno):
		self.caseno = caseno
		self.sol = []
		self.run()

for caseno in range(1,read(int)+1): print Case(caseno);

"""
L=[2,4,6,8,10]
i = find_heavier_block(L,9)
print i
i = find_heavier_block(L,7)
print i,L[i]
i = find_heavier_block(L,5)
print i,L[i]
i = find_heavier_block(L,3)
print i,L[i]
i = find_heavier_block(L,1)
print i,L[i]
"""
