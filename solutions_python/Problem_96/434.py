#!/usr/bin/python2.7 -tt

"""
Shikhar Srivastav
Google Code Jam 2012
Problem 2
"""

from math import *

def main():
	f=open("inp.txt")
	N=int(f.readline())
	ans=[]
	for line in f:
		words=line.split()
		surp=int(words[1])
		p=int(words[2])
		abv_p=0
		for w in words[3:]:
			if(int(w)==0):
				if(int(w)>=p): abv_p+=1
				continue
			x=float(w)/3
			c=ceil(x)
			f=modf(x)[0]
			if(c>=p):
				abv_p+=1
			elif c+1>=p and (f<0.3 or f>0.4) and surp>0 :
				abv_p+=1
				surp-=1
		ans.append(abv_p)
	for i in range(N):
		print "Case #"+str(i+1)+": "+str(ans[i])
				

if __name__=='__main__':
	main()
