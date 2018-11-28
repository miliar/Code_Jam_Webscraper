import itertools
from fractions import gcd
from math import sqrt
from bisect import bisect_left , bisect_right
import heapq
from collections import deque , defaultdict , Counter
from itertools import combinations as C
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

def solve(str_ , k):
	ix = 0
	l = len(str_)
	ls = [1 if i == '+' else 0 for i in str_]
	cnt = 0
	while ix < l:
		if ls[ix] == 0:
			if ix + k <= l:
				for j in xrange(ix , ix + k):
					ls[j] ^= 1
			cnt += 1
		ix += 1
	if 0 not in ls:
		return cnt
	else:
		return "IMPOSSIBLE"
		

T = input()
for _ in xrange(T):
	a , b = raw_input().split()
	b = int(b)
	print "Case #%s:" %(_+1),solve(a,b)
		
