from math import *
import math

def entre():
	n=int(input())
	inpute=[[] for i in range(n)]
	for i in range(n):
		s=input()
		s=s.split()
		inpute[i]=[int(s[0]),int(s[1])]
	return inpute
	
def min(a,b):
	if a<b:
		return a
	else:
		return b
		
def max(a,b):
	if a>b:
		return a
	else:
		return b

E=entre()

nb=0
for T in E:
	nb+=1
	c0=T[0]
	c=T[0]
	p=T[1]
	r=0
	m0=1
	while p>m0:
		r+=1
		m0+=2**r
	m0-=2**r
	p1=max(p-m0,1)
	for x in range(r):
		c=math.floor((c-1)/2)+(c-1)%2
	c=max(c-1,0)
	if p1>c0%(2**r)+1:
		c=max(c-1,0)
	print("Case #"+str(nb)+": "+str(math.floor(c/2)+c%2)+" "+str(math.floor(c/2)))

