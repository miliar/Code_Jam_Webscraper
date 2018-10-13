#!/usr/local/bin/python

def readlist(fn): return map(fn,raw_input().split())
def read(fn): return fn(raw_input())

class Case:

	def run(self):
		pos1  = read(int)-1	
		grid1 = [set(readlist(int)) for i in range(4)]
		pos2  = read(int)-1
		grid2 = [set(readlist(int)) for i in range(4)]
		
		comm  = grid1[pos1] & grid2[pos2]
		if len(comm) == 1: self.sol = comm.pop()
		elif len(comm) > 1: self.sol = 'Bad magician!'
		else: self.sol = 'Volunteer cheated!'

	def __str__(self):
		return "Case #%d: %s" % (self.caseno,str(self.sol))

	def __init__(self,caseno):
		self.caseno = caseno
		self.sol = -1
		self.run()

for caseno in range(1,int(raw_input())+1): print Case(caseno);

