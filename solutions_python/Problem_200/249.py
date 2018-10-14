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

def solve(n,k):
	ls = []
	st = n - 1
	if (st % 2 == 1):
		put = (st/2 , st/2+1)
	else:
		put = (st/2 , st/2)
	queue = deque([put])
	while queue:
		node = queue.popleft()
		#print node
		ls.append(node)
		if (node > (0,0)):
			stx = node[0] - 1
			if (stx % 2 == 1):
				putx = (stx/2 , stx/2+1)
			else:
				putx = (stx/2 , stx/2)
			sty = node[1] - 1
			if (sty % 2 == 1):
				puty = (sty/2 , sty/2+1)
			else:
				puty = (sty/2 , sty/2)
			if (putx >= (0,0)):queue.append(putx)
			if (puty >= (0,0)):queue.append(puty)
	ls.sort(reverse = True)
	#print ls
	a,b = max(ls[k-1]),min(ls[k-1])
	return str(a) + " " + str(b)
	
def logme(n,k):
	seq = []
	while k > 1:
		seq.append(k)
		k /= 2
	print seq
	st = n - 1
	if (st % 2 == 1):
		put = (st/2+1 , st/2)
	else:
		put = (st/2 , st/2)
	for i in seq:
		print put , i
		if i % 2 == 0:
			st = put[0] - 1
		else:	st = put[1] - 1
		if (st % 2 == 1):
			put = (st/2 + 1, st/2)
		else:
			put = (st/2 , st/2)
	a , b = put
	print put
	return str(a) + " " + str(b)

def kyahe(int_):
	while int_ > 9:
		ls = map(int , list(str(int_)))
		if sorted(ls) == ls:
			return int_
		int_ -= 1
	return int(int_)
def bc(kid):
	st = list(str(kid))
	if len(st) <= 1:
		return int(''.join(st))
	for i in xrange(len(st) - 1, -1 , -1):
		if i - 1 >= 0:
			t = i - 1
			a,b = int(st[i]),int(st[t])
			if b > a:
				st[t] = str(b-1)
				for ix in xrange(i,len(st)):st[ix] = '9'
	str_ = ''.join(st)
	str_ = str_.lstrip('0')
	return int(str_)
				
			
		
T = input()
for _ in xrange(T):
	n  = input()
	print "Case #%s:" %(_+1),bc(n)
	#print logme(n,k)

		
