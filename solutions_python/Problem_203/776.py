import itertools
from fractions import gcd
from math import sqrt
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
sys.stdin = open('input.txt' ,'r')
sys.stdout = open('output.txt' , 'w')
###

#SHIT GOES BELOW
def recur(grid , x , y , ch):pass
	
		
T = input()
for _ in xrange(T):
	r, c = get(int)
	grid = []
	chose = set()
	for j in xrange(r):
		grid.append(Ls())
		for ix in grid[j]:
			if ix != '?':chose.add(ix)
	chose = list(chose)
	har = dict()
	for i in xrange(r):
		for j in xrange(c):
			if grid[i][j] != '?':
				if (grid[i][j]) not in har:
					har[grid[i][j]] = [(i,j)]
				else:
					har[grid[i][j]].append((i,j))
	vis = dict()
	for ix in har:
		if len(har[ix]) > 1:
			#find rect
			yi,xi = [],[]
			for jx in har[ix]:
				xi.append(jx[0])
				yi.append(jx[1])
			rectx,recty = min(xi),min(yi)
			recx,recy = max(xi),max(yi)
			for i in xrange(rectx,recx+1):
				for j in xrange(recty,recy+1):
					grid[i][j] = ix
			vis[ix] = True
	#row bhar do
	#print har
	for ix in har:
		if len(har[ix]) == 1:
			#print grid,ix
			row,col = har[ix][0][0],har[ix][0][1]
			coly = col
			colx = col
			for j in xrange(col+1,c):
				if grid[row][j] == '?':
					grid[row][j] = ix
				else:break
				coly = j
			for j in xrange(col-1,-1,-1):
				if grid[row][j] == '?':
					grid[row][j] = ix
				else:break
				colx = j
			xi = row - 1
			while xi >= 0:
				if grid[xi][colx:coly+1].count('?') ==  coly-colx+1:
					#print grid[xi][colx:coly+1],xi
					for j in xrange(colx,coly+1):
						grid[xi][j] = ix
				else:break
				xi -= 1
			xi = row + 1
			while xi < r:
				if grid[xi][colx:coly+1].count('?') ==  coly-colx+1:
					#print grid[xi][colx:coly+1],xi
					for j in xrange(colx,coly+1):
						grid[xi][j] = ix
				else:break
				xi += 1
			vis[ix] = True
			#print grid,ix
	print "Case #%s:" %(_+1)
	for i in xrange(r):
		print ''.join(grid[i])
	
	#print "Case #%s:" %(_+1),ans

		
