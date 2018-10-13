#!/usr/local/bin/python

def readlist(fn): return map(fn,raw_input().split())
def read(fn): return fn(raw_input())

class Case:

	def run(self):
		A,B,K = readlist(int)
		n = 0
		for a in range(A):
			for b in range(B):
				if a&b < K: n+=1
		self.sol=n



		pass
	def __str__(self):
		return "Case #%d: %s" % (self.caseno,str(self.sol))

	def d(s):
		if self.caseno not in self.debugcase: return
		print ' ',self.caseno,' ',s

	def __init__(self,caseno):
		self.debugcase = [] # []
		self.caseno = caseno
		self.run()

for caseno in range(1,read(int)+1): print Case(caseno);

