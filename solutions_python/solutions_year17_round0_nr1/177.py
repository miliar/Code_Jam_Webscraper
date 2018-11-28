#!/usr/bin/pypy
import sys
if sys.version_info[0]<=2:
	range=xrange
	input=raw_input

def solve0(s,k):
	n=len(s)
	flips=0
	for i in range(n-k+1):
		if s[i]=="-":
			flips+=1
			for j in range(k):
				s[i+j]=("-","+")[s[i+j]=="-"]
	for i in range(n):
		if s[i]=="-":
			return "IMPOSSIBLE"
	return flips

cases=int(input().strip())
for cs in range(1,cases+1):
	s,k=input().strip().split()
	s=list(s)
	k=int(k)
	print("Case #"+str(cs)+": "+str(solve0(s,k)))
