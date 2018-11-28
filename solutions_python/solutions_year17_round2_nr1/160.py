#from __future__ import division
import itertools
from fractions import gcd
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
sys.stdin = open('A-small-attempt0.in' ,'r')
#sys.stdin = open('A-large-attempt0.in' ,'r')
#sys.stdin = open('A-small-practice.in' ,'r')

sys.stdout = open('output.txt' , 'w')
###

#may the force with me.

for x in xrange(input()):
	#n = input()
	d,n = get(int)
	st = []
	for i in xrange(n):
		a,b = get(int)
		st.append((a,b))
	st.sort()
	ans = 1 << 30;
	tim = -1
	res = 1 << 50;
	print 'Case #%d:' %(x+1) ,
	for i in xrange(n):
		start = st[i][0]
		speed = st[i][1]
		ti = 0
		for j in xrange(i+1,n):
			sx,sp = st[j][0],st[j][1]
			ps = sx - start
			px = speed - sp
			try:
				time = ps/float(px)
				#print time,speed,start
				if time >= 0 and start + time*speed <= d and sx + time*sp <=d:
					#speed  = min(speed,sp)
					ti += time
					start += (time*speed)
					speed = min(speed ,sp)
			except:pass
			#print start,speed
		ti += (d - start)/float(speed)
		ans = min(ans,speed)
		#print ans,ti , d/ti
		res = min(res,d/ti)
	print  res
	#pass
	
	
	
		
			
			
		
