#!/usr/local/bin/python

def readlist(fn): return map(fn,raw_input().split())
def read(fn): return fn(raw_input())

class Case:
	def f(self,C,F,X,r=2):
		if abs(C/r-X/r) < 0.000001 or r >20: return X/r
		print C/r
		return min(self.f(C,F,X,F+r)+C/r, X/r)

	def run(self):
		C,F,X = readlist(float)
		#self.sol = self.f(C,F,X) # stack overflow....

		r = 2 # starting cookie rate
		# (cost to build 0~nth factory, time to make X with nth factories)
		prev = (0,X/r) 
		while abs(X/r-X/(r+F)) > 0.000001: 
			r += F	# build new factory
			curr = C/(r-F)+prev[0], X/r
			if sum(curr) > sum(prev): # stop if building new factory no longer help
				self.sol = sum(prev)
				return
			prev = curr

	def __str__(self):
		return "Case #%d: %0.6f" % (self.caseno,self.sol)

	def __init__(self,caseno):
		self.caseno = caseno
		self.sol = -1
		self.run()

for caseno in range(1,read(int)+1): print Case(caseno);
