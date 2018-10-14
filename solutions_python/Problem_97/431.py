#!/usr/bin/python2.7 -tt

"""
Shikhar Srivastav
Google Code Jam 2012
Problem 3
"""

from math import *

def rotate(x):
	return x[-1]+x[:-1]
	
def main():
	f=open("inp.txt")
	N=int(f.readline())
	ans=[]
	ans2=[]
	for line in f:
		words=line.split()
		A=int(words[0])
		B=int(words[1])
		s=set()
		for n in range(A,B+1):
			l=len(str(n))-1
			r=str(n)
			for i in range(l):
				r=rotate(r)
				m=int(r)
				if(m>n and m<=B):
					s.add((n,m))
		ans.append(len(s))
		ans2.append(s)
		
	for i in range(N):
		print "Case #"+str(i+1)+": "+str(ans[i])

if __name__=='__main__':
	main()
