#!/usr/bin/python

import sys
import math	
import Queue
from datetime import datetime

startTime = datetime.now()
sys.setrecursionlimit(20000)

def readn(n):
	return [raw_input().strip() for i in range(n)]
def read():
	return raw_input().strip()
def readints():
	return map(int, read().split())
def readint():
	return readints()[0]
def wl(n, o):
	print("Case #{0}: {1}".format(n, o))

def solve(N, M, data):
	for i in range(N-1):
		for j in range(M-1):
			if(data[i][j]=='#'):
				if data[i][j+1]!='#' or data[i+1][j]!='#' or data[i+1][j+1]!='#': return "Impossible"
				data[i][j:j+2]="/\\"
				data[i+1][j:j+2]="\/"
	for i in range(M):
		if data[N-1][i]=="#": return "Impossible"
	for i in range(N):
		if data[i][M-1]=="#": return "Impossible"
	return None
	
T = readint()
for TT in range(T):
	N, M = readints()
	data = list()
	for i in range(N):
		data.append(list(read()))
	wl(TT+1,"")
	if(solve(N,M,data)=="Impossible"):
		print("Impossible")
	else:
		for i in range(N):
			print("".join(data[i]))
	
	
#print(datetime.now()-startTime)