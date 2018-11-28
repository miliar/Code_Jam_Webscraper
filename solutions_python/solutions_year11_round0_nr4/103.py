#!/usr/bin/python
t=input()
for ti in range (1,t+1):
	all=0.0
	n=input()
 	s=raw_input().split()
 	s=map(lambda i:int(i),s)
 	lenn=len(s)
 	cou=lenn
 	mark=[]
 	for j in range (0,lenn):
 		if(s[j]==j+1):
 			mark.append(0)
 			cou-=1
 		else :
 			mark.append(1)
 #	print s
	while(cou>0):
		jh=[]
		i=0
		td=0
		while(mark[i]==0):
			i=i+1
		jh.append(i+1)
		mark[i]=0
		cou-=1
		td+=1
		i=s[i]-1
		
 #		print "s[",i,"]=",s[i]
		while(not jh.__contains__(s[i])):
			mark[i]=0
			i=s[i]-1
			jh.append(i+1)
			cou-=1
			td+=1
 #		print jh
		mark[i]=0
#		print mark
		cou-=1
		td+=1
		all+=td
#		print "cou:%d td:%d" %(cou,td)
#	 	print "mark",mark
	print "Case #%d: %.6f" %(ti,all)

