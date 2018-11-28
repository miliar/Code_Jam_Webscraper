#!/usr/bin/python

import sys

class triplets:
	def __init__(self,t):
		self.t = t
	
	def getTriplets(self,surprising = False):
		if (self.t % 3 == 0):
			if(self.t == 0): return (0,0,0)
			if surprising:
				return ((self.t/3)+1,self.t/3,(self.t/3)-1)
			else:
				return (self.t/3,self.t/3,self.t/3)
		else:
			if surprising:
				if(self.t%3 == 2):
					return (self.t/3,(self.t/3),(self.t/3)+2)
				else:
					return (self.t/3,(self.t/3)+1,(self.t - ((self.t/3) + (self.t/3)+1)))
			else:
				return (self.t/3,(self.t/3)+1,(self.t - ((self.t/3) + (self.t/3)+1)))
	
	def is_greater_than_p(self,p,surprising = False):
		if (self.t/3 >= p): 
			return True
		
		t = self.getTriplets(surprising)
		
		if any(x >= p for x in t): 
			return True
		else: 
			return False

class testcase:
	def __init__(self,n,s,p):
		self.n = n
		self.s = s
		self.p = p
		self.tlist = []
		self.greater_than_p = 0
	
	def addt(self,t):
		t1 = triplets(t)
		self.tlist.append(t1)
	
	def __str__(self):
		for x in self.tlist:
			print str(x.getTriplets()) + ' ',
		return "n = "+str(self.n)+"\ns = "+str(self.s)+"\np = "+str(self.p)+"\n> p = "+str(self.greater_than_p)
	
	def num_greater_than_p(self):
		self.greater_than_p = 0
		scount = 0
		for t in self.tlist:
			if t.is_greater_than_p(self.p):
				self.greater_than_p += 1
			else:
				if ((self.s - scount)> 0):
					#print "Surprising : "+ str(scount)
					if t.is_greater_than_p(self.p,surprising = True):
						self.greater_than_p += 1
						scount += 1

def read_inp():
	N = int(inp.readline())
	n = N
	testcases = []
	while n > 0:
		line = inp.readline()[:-1].split()
		line = [int(x) for x in line]
		t = testcase(line[0],line[1],line[2])
		m = line[0]
		while m > 0:
			t.addt(line[m+2])
			m = m - 1
		testcases.append(t)
		n = n - 1
	return N,testcases

inp = sys.stdin
N,testcases = read_inp()
for i,t in enumerate(testcases):
	t.num_greater_than_p()
	print "Case #"+str(i+1)+": "+str(t.greater_than_p)

