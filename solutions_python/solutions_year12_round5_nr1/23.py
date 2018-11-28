#!/usr/bin/python

import sys

class Item:
	def __init__(self,p,s):
		self.p = p
		self.s = s
	def __lt__(self, other):
		if self.p < other.p: return True
		elif self.p > other.p: return False
		else: return self.s < other.s
	def __eq__(self,other):
		return self.p == other.p and self.s == other.s

def itemcmp(a,other):
	if a.p <= other.p: return True
	else: return a.s <= other.s


def do():
	N = [int(x) for x in sys.stdin.readline().split()]
	l = [int(x) for x in sys.stdin.readline().split()]
	items = [int(x) for x in sys.stdin.readline().split()]
	idxitems = [ Item(100-items[i],i) for i in range(0, len(items))]
	idxitems.sort()
	for i in range(0,len(idxitems)):
		#ret += " (%s,%s)" % (100 - idxitems[i].p, idxitems[i].s)
		sys.stdout.write(' %s' % idxitems[i].s)
	print("")

T = int(sys.stdin.readline())

for i in range(1,T+1):
	sys.stdout.write("Case #%s:" % i)
 	do()
