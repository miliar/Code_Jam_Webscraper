from __future__ import with_statement
from math import *

maxValue = 2**31
class LeafNode(object):
	isLeaf = True 
	def __init__(self, value):
		self.value = value
	
	def mirror(self):
		self.value = 1 - self.value
		
	def process(self):
		if self.value:
			return 0
		else:
			return maxValue

class InnerNode(object):
	def __init__(self, gate, changeable):
		self.gate = gate
		self.changeable = changeable
	
	def bind(self, l, r):
		self.l = l
		self.r = r
		
	def mirror(self):
		self.gate = 1 - self.gate
		self.l.mirror()
		self.r.mirror()
	
	def process(self):
		lv = self.l.process()
		rv = self.r.process()
		if self.gate:
			if self.changeable:
				return min(lv + rv, min(lv, rv) + 1)
			else:
				return lv + rv
		else:
			return min(lv, rv) 
			
		

def processFile(fin, fout):
	numCases = int(fin.readline())
	for caseNumber in xrange(1, numCases + 1):
		lineItems = fin.readline().strip().split()
		print lineItems
		nodeCount, desiredValue = map(int, lineItems)
		nodes = []
		
		for i in xrange((nodeCount - 1) / 2):
			lineItems = fin.readline().strip().split()
			nodes.append(InnerNode(*map(int, lineItems)))
			
		for i in xrange((nodeCount + 1) / 2):
			lineItems = fin.readline().strip().split()
			nodes.append(LeafNode(int(lineItems[0])))

		for i in xrange((nodeCount - 1) / 2):
			nodes[i].bind(nodes[i*2 + 1], nodes[i*2 + 2])
		
		if desiredValue == 0:
			nodes[0].mirror()
	
		res = nodes[0].process()
		if res >= maxValue:
			res = 'IMPOSSIBLE'
		s = "Case #" + str(caseNumber) + ": " + str(res)
		print s
		print >> fout, s


task = "A"

with open(task + "-small.in") as f:
	with open(task + "-small.out", "w") as fout:
		processFile(f, fout)
print "OK!"
with open(task + "-large.in") as f:
	with open(task + "-large.out", "w") as fout:
		processFile(f, fout)
