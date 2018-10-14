from __future__ import division
import itertools
from fractions import gcd
from heapq import *
from math import *
from bisect import bisect_left , bisect_right
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
sys.stdin = open('C-small-1-attempt0.in' ,'r')
#sys.stdin = open('A-large-attempt0.in' ,'r')
#sys.stdin = open('A-small-practice.in' ,'r')

sys.stdout = open('output.txt' , 'w')
###

from networkx.algorithms import bipartite
import networkx as nx

#may the force with me.

def outfile(n,res):
	print 'Case #%d: %0.8f' %(n ,res) 
	#print res
def outterm(n,res):
	print >> sys.stderr,'Case #%d: %0.8f' %(n ,res)
	#print >> sys.stderr, res

def brute( n, k ):
	global st , x
	ls = range(n)
	mxi = 0;area = 0
	result = dict()
	for i in C(ls,k):
		bs = []
		for j in i:
			bs.append(st[j])
		bs.sort(reverse = True)
		area = pi*2*bs[0][1]*bs[0][0]
		for ix in xrange(1,len(bs)):
			area += pi*abs(bs[ix-1][0]**2 - bs[ix][0]**2)
			area += 2 * pi * bs[ix][1]*bs[ix][0]
		area += pi * bs[-1][0]**2
		mxi = max(mxi , area)
		result[mxi] = bs[:]
	#print result[mxi]
	return 'Case #%d: %0.8f' %(x+1 ,area) 
	#outterm(x+1,mxi)


def solve(nx):
	global h,u
	sm = 0
	for i in h:
		if i <= nx:
			sm += (nx - i)
	return sm <= u

for x in xrange(input()):
	n , m = get(int)
	u = float(raw_input())
	h = get(float)
	low = 0.00
	high = 1.00
	#print solve()
	ans = 0
	for i in xrange(300):
		mid = low + (high - low) / 2.0
		if solve(mid):
			low = mid
			#print mid
			anx = 1
			for xi in h:
				if xi <= mid:
					anx *= mid
				else:
					anx *= xi
			ans = max(ans , anx)
		else:
			high = mid
	print 'Case #%d: %0.8f' %(x+1 ,ans) 
	
	
	
	
	
		
	

			
		
		
	
			
	
	
					
			
			
	
	
	
		
			
			
		
