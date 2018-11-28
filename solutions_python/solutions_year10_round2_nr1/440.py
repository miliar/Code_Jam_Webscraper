#!/usr/bin/python

from sys import stdin


def fixIt():
	T = int(stdin.readline())
	for iT in xrange(1, T + 1):
		(N, M) = [int(v) for v in stdin.readline().split()]
		dirDict = {}
		for iN in xrange(N):
			dList = stdin.readline()[:-1].split('/')[1:]
			parent = dirDict
			for d in dList:
				if not parent.has_key(d):
					parent[d] = {}
				parent = parent[d]
			parent = dirDict
		steps = 0
		for iM in xrange(M):			
			dList = stdin.readline()[:-1].split('/')[1:]
			parent = dirDict
			for i in xrange(len(dList)):
				d = dList[i]
				if parent.has_key(d): 
					parent = parent[d]
					continue
				else:
					steps += len(dList) - i
					for v in dList[i:]:
				 		parent[v] = {}
						parent = parent[v]
				 	break
		print "Case #%d: %d" %(iT, steps)

if "__main__" == __name__:
	fixIt()
