# -*- coding: utf-8 -*-
# Google Code Jam
# Create Date: 2014-04-10
# Created by: buaamm
#--------------------------------------------------------------------
import sys
import os

def nextint():
	return (int)(fr.readline())

def nextints():
	return map(int, next().strip().split())
	
def next():
	return fr.readline()

def write(s):
	fw.write(str(s))
	
def writeline(s):
	fw.write(str(s) + "\n")

def repeat(s, r):
	for i in range(r):
		fw.write(s)

def reprep(s, len, r):
	for i in range(r):
		repeat(s, len)
		write("\n")

def draw_single(n,m):
	write("c")
	repeat("*", m-1)
	write("\n")
	reprep("*", m, n-1)
def draw_line(a,b):
	repeat(".", a)
	repeat("*", b)
	write("\n")



#--------------------------------------------------------------------
def solve():
	n = nextint()
	arr = nextints()
	ans = 0
	while n > 1:
		MIN = 1000000001
		MININD = -1
		for i in range(n):
			if arr[i] < MIN:
				MIN = arr[i]
				MININD = i
		
		ans += min(MININD, n - 1 - MININD)
		arr = arr[:MININD]+arr[MININD+1:]
		n -= 1
		
	write("%d\n" % ans)
	
	#	Solve
	
	#write("%d\n" % dp[39][0][0])
	
#--------------------------------------------------------------------
if __name__ == "__main__": ##__name__: [filename].py
	print "Hello, Main."
else:
	global fr, fw
	prob_name = "B-large"

	fr = open(prob_name + '.in', 'r')
	fw = open(prob_name + '.out', 'w')
	cas = (int)(fr.readline())
	for cs in range(cas):
		write("Case #%d: " % (cs+1) )
		solve()
	fr.close()
	fw.close()
#--------------------------------------------------------------------


