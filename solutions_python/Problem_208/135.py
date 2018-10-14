from __future__ import division
import itertools
from fractions import gcd
from heapq import *
from math import *
from bisect import bisect_left , bisect_right
import heapq
from collections import deque , defaultdict , Counter
from itertools import combinations as C
from random import randrange as rd
def Ls():
	return list(raw_input())
def get(a):
	return map(a , raw_input().split())
def Int():
	return int(raw_input())
def Str():
	return raw_input()

###REDIRECT IO
import sys
sys.stdin = open('C-large.in' ,'r')
#sys.stdin = open('A-large-attempt0.in' ,'r')
#sys.stdin = open('A-small-practice.in' ,'r')

sys.stdout = open('output.txt' , 'w')
###

#may the force with me.
N = 10
def Dijkstra(graph, start):
	global N
	A = [None] * N
	queue = [(0, start)]
	while queue:
	    path_len, v = heappop(queue)
	    if A[v] is None: # v is unvisited
	        A[v] = path_len
	        for w, edge_len in graph[v].items():
	            if A[w] is None:
	                heappush(queue, (path_len + edge_len, w))
	return [0 if x is None else x for x in A] 

for x in xrange(input()):
	n , q = get(int)
	st = []
	har = dict()
	print 'Case #%d:' %(x+1),
	for i in xrange(n):
		a,b = get(int)
		st.append((a,b))
		har[i] = True
	gr =  defaultdict(dict)	
	grid = [];dist = []
	for i in xrange(n):
		grid.append(get(int))
		ls = [1 << 40 if i == -1 else i for i in grid[i]]
		dist.append(ls)
	N = n
	#dist = []
	for k in xrange(n):
		for i in xrange(n):
			for j in xrange(n):
				dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j])
	for i in xrange(n):
		for j in xrange(n):
			if i != j and grid[i][j] != -1 and i in har:
				tot = grid[i][j]
				time = tot / float(st[i][1])
				if tot <= st[i][0]:
					gr[i][j] = time
			
	for i in xrange(n):
		for j in xrange(n):
			if dist[i][j] != 1 << 40 and i != j and i in har:
				tot = dist[i][j]
				time = tot / float(st[i][1])
				if tot <= st[i][0]:
					gr[i][j] = time
	#s,e = get(int)	
	
	dist = [[1 << 40 for j in xrange(n)] for i in xrange(n)]
	for i in gr:
		for j in gr[i]:
			dist[i][j] = gr[i][j]
	for k in xrange(n):
		for i in xrange(n):
			for j in xrange(n):
				dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j])
	for qx in xrange(q):
		a , b = get(int)
		print dist[a-1][b-1],
	print
			
	
	
					
			
			
	
	
	
		
			
			
		
