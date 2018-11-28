#Ricardo Corral Corral - mayo 6, 2012
import sys
from sys import stdin
from collections import deque

visitados = set()

diamante = ''


G = {}
def diamondd(s):
	if s in visitados:
		global diamante
		diamante = 'Yes'
		return 
	visitados.add(s)
	for i in G[str(s)]:
		diamondd(i)


fin = open(sys.argv[1])

T = int(fin.readline().strip())

for i in xrange(1,T+1):
	G.clear()
	N= int(fin.readline().strip())
	for j in xrange(N):
		Mi = map(int,fin.readline().strip().split())
		M = Mi[0]
		Mi=Mi[1:]
		s = []
		for k in xrange(M):
			s.append(str(Mi[k]))
		G[str(j+1)] = s
	diamante = 'No'
	for j in xrange(1,N+1):
		visitados.clear()
		diamondd(j)
		if diamante == 'Yes':
			break
	print 'Case #'+str(i)+': ' + diamante 
