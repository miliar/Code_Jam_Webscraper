#!/usr/local/bin/python

def readlist(fn): return map(fn,raw_input().split())
def read(fn): return fn(raw_input())

def get_rll(s):
	L = []
	curchar  = s[0]
	curcount = 0
	n = len(s)
	for i,c in enumerate(s):
		if c == curchar:
			curcount+=1
			continue
		L.append( (curchar,curcount) )	
		curcount = 1
		curchar  = c
	L.append( (curchar,curcount) )
	return L

def is_possible(L):
	# check len
	n = len(L[0])
	for l in L:
		if len(l) != n: return False
	
	for i in range(n):
		curchar = L[0][i][0]
		for l in L:
			if l[i][0] != curchar: return False
	return True

def count_changes(L):
	n = len(L[0])
	m = len(L)
	M = []		
	for i in range(n):
		avg = sum( [l[i][1] for l in L] )/m
		M.append(avg)
	
	acc = 0
	for i in range(n):
		acc += sum( [abs(l[i][1]-M[i]) for l in L])

	return acc

class Case:
	def run(self):
		N = read(int)
		L = [get_rll(read(str)) for i in range(N)]
		if not is_possible(L):
			self.sol = 'Fegla Won'
		else:
		  self.sol = count_changes(L)

	def __str__(self):
		return "Case #%d: %s" % (self.caseno,str(self.sol))

	def d(s):
		if self.caseno not in self.debugcase: return
		print ' ',self.caseno,' ',s

	def __init__(self,caseno):
		self.caseno = caseno
		self.run()

for caseno in range(1,read(int)+1): print Case(caseno);

