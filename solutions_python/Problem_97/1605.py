#!usr/bin/env python
# -*- coding: iso-8859-1 -*-

#Function to generate list of digits of an integer. 
def getlist(n) :
  N=n
  l=[]
  L=[]
  while N>0 :
    l.append(N%10)
    N=N//10
  for i in range(len(l)) :
    L.append(l[N-i-1])
  return L

#Function to generate a number from an entered list.
def getnum(l) :
  N=len(l)
  num=0
  for i in range(len(l)) :
    num += l[i]*10**(N-i-1)
  return num

# Function to generate all possible recycled numbers for a given integer.
def recycle(n) :
  L=getlist(n)
  N=len(L)
  flist=[]
  for i in range(1,N) :
    j=0
    l1=[]
    l2=[]
    l3=[]
    while j<i :
      l1.append(L[N-1-j])
      j+=1
    P1=len(l1)
    for k in range(0,N-j) :
      l2.append(L[k])
    for p in range(0,N) :
      if p< P1 :
	l3.append(l1[P1-1-p])
      if p>=P1 :
	l3.append(l2[p-P1])
    if len(l3)==N :
      flist.append(getnum(l3))
  return sorted(flist)

#print recycle(12345)  
f=open('C-small-attempt0.in','rt')
fo=open('output.txt','wt')
s=f.readline()
num=int(str.split(s,'\n')[0])

for a in range(num):
	s=f.readline()
	k=str.split(s,' ')
	A=int(k[0])
	B=int(k[1])
	R1=[]
	R=[]
	for n in range(A,B+1) :
	  R=recycle(n)
	  for p in range(len(R)):
	    if A <= n < R[p] <= B :
	      R1.append(R[p])
	fo.write('Case #%d: %d\n'%(a+1,len(R1)) )
	
fo.close()

