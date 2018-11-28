# -*- coding: utf-8 -*-

def ch (v1,pos1,j1):
	i=0
	s=list(v1)
	#print "0000LEN="+str(j1)
	#print "0000PH="+str(pos1)
	print "IN="+v1


	while i<j1:
		if (s[pos1+i]=='-'):
			s[pos1+i]='+'
			i=i+1
		else: 
			s[pos1+i]='-'
			i=i+1
	print "OUT="
	print "".join(s)
	return "".join(s)
    

def myfunc(v,j):
	mj=0
	print "GOT="+v
	while (mj<len(v)):
		pos=-1
		kk=0
		while kk<len(v):
			if (v[kk]=='-'):
				pos=kk
				break;
			else :
				kk=kk+1
		print v	
		print "POS="+str(pos)
		
		if(pos==-1):
			return mj
		if(len(v)<(pos+j) ):
			return 'IMPOSSIBLE'
		if(len(v)>=(pos+j) ):
			v=ch(v,pos,j)
			mj=mj+1
		
	
file = open('a.txt', 'r') 
k=file.readline()
jj=int(k)

ii=1

file1= open('b.txt','w')

while ii<=jj:
	k=file.readline()
	m=k.split(' ')
	print m[0]
	m1=m[1].split('\n')
	print m1[0]
	fj=int(m1[0])
	print "LEN="+str(fj)
	ff=myfunc(m[0],fj)
	file1.write('Case #'+str(ii)+': '+str(ff)+'\n')
	print "-------------------------------"
	ii=ii+1
	
