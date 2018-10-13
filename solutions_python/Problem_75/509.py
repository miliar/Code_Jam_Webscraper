#! /usr/bin/env python

from sys import stdin
import collections


def process(elements, opposed, pairs):
	stk=[]
	contains=collections.Counter()
	for item in elements:
		#print "\n > ",item,stk
		if len(stk) and pairs[item][stk[-1]]!=-1:
			tmp=stk.pop()
			stk.append(pairs[item][tmp])
			contains[tmp]-=1
			contains[pairs[item][tmp]]+=1
	
		elif any(x in opposed[item] for (x,v) in contains.items() if v>0):
			stk=[]
			contains=collections.Counter()
		else:
			stk.append(item)
			contains[item]+=1
	return stk

def to_int(item):
	return ord(item)-65

def to_char(item):
	return chr(item+65)

if __name__=='__main__':
	cases=int(stdin.readline())
	for case in xrange(1,cases+1):
		instream=collections.deque(stdin.readline().split())
		C=int(instream.popleft())
		pairs=[[-1 for i in xrange(27)] for j in xrange(27)]
		for i in xrange(C):
			data=map(to_int,instream.popleft())
			#print data
			pairs[data[0]][data[1]], pairs[data[1]][data[0]]=data[2],data[2]
		D=int(instream.popleft())
		opposed=collections.defaultdict(set)
		for i in xrange(D):
			data=map(to_int,instream.popleft())
			opposed[data[0]].add(data[1])
			opposed[data[1]].add(data[0])
		instream.popleft() # discard N, we don't need it
		elems=map(to_int,instream.popleft())
		print "Case #%d: [%s]"%(case,", ".join(map(to_char,process(elems,opposed,pairs))))

	
	
				
