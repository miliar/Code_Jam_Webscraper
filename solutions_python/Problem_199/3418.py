#!/bin/python

def findans(inp):
	k=inp[1]
	inp=inp[0]
	negs="-"*int(k)
	pos="+"*int(k)
	s1=""
	if k>1:
		s1="-"+"+"*(int(k)-1)+"-"
	else:
		s1="-"
	s2=""
	if k>1:
		s2="+"+"+"*(int(k)-1)+"+"
	else:
		s2="+"
	s3="-"+"+"*(int(k))+"-"
	s4="+"+"+"*(int(k))+"+"
	count=0
	while True:
		if s1 in inp:
			inp=inp.replace(s1,s2,1)
			count+=2
		elif s3 in inp:
			inp=inp.replace(s3,s4,1)
			count+=3
		elif negs in inp:
			inp=inp.replace(negs,pos,1)
			count+=1
		else:
			break
	return count,inp

tcases=int(raw_input())
j=1
while tcases>0:
	inp = raw_input()
	inp=inp.split(" ")
	(count,inp)=findans(inp)
	if "-" in inp:
		print "Case #"+str(j)+": "+"IMPOSSIBLE"
	else:
		print "Case #"+str(j)+": "+str(count)		
	j=j+1
	tcases-=1