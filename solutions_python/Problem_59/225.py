#! /usr/bin/python
from collections import deque
from sys import stdin

def insert(node,path):
	if len(path)==0:
		return 0
	elif path[0] in node:
		cur=path.popleft()
		return insert(node[cur],path)
	else:
		cur=path.popleft()
		node[cur]={}
		return 1+insert(node[cur],path)
		
if __name__=='__main__':
	T=int(stdin.readline())
	for case in xrange(1,T+1):
		N,M=map(int,stdin.readline().split())
		paths=[stdin.readline() for i in xrange(N)]
		paths=[p.replace("/",' ').split() for p in paths]
		root={}
		for path in paths:
			p=[x for x in path if len(x)]
			insert(root,deque(p))
		queries=[stdin.readline() for i in xrange(M)]
		queries=[q.replace('/',' ').split() for q in queries]
		answer=sum(insert(root,deque(query)) for query in queries)
		print "Case #%d: %d"%(case,answer)
		
