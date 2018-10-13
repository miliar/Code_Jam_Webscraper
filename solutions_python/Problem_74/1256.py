#!/usr/bin/env python
import sys

file=open(sys.argv[1],'r')
case=int(file.readline().strip())
fout=open('A.out','w')
for i in range(case):
	line=file.readline().split()
	taskn=int(line[0])
	line=line[1:]
	t=[]
	pos=[1,1]
	for j in range(taskn):
		if line[j*2]=='O':
			ro=0
		else:
			ro=1
		bu=int(line[j*2+1])
		walkstepnow=abs(bu-pos[ro])
		if j>0:
			if ro==pre_ro:
				totalstep=totalstep+walkstepnow+1		
				cnt=cnt+1
			else:
				t.append([walkstep, totalstep,cnt])
				walkstep=walkstepnow
				totalstep=walkstepnow+1
				cnt=1
		else:
			walkstep=walkstepnow
			totalstep=walkstepnow+1
			cnt=1
		pos[ro]=bu
		pre_ro=ro
	t.append([walkstep, totalstep,cnt])
	
	ans=0
	for k in range(len(t)):
		if k==0: continue
		d=-min(t[k-1][1],t[k][0])
		t[k][0]=t[k][0]+d
		t[k][1]=t[k][1]+d
		
	ans=0
	for k in range(len(t)):
		ans=ans+t[k][1]
		
#	for k in range(len(t)):
#		if k==0: continue
#		if t[k][0]<t[k-1][1]:
#			ans=ans+t[k-1][1]
#			d=-min(t[k-1][1],t[k][0])
#			t[k][0]=t[k][0]+d
#			t[k][1]=t[k][1]+d
#		#	if k==len(t)-1:
#	#			ans=ans+t[k][2]
#	#	else:
#	#		if k==len(t)-1:
#	#			ans=ans+t[k][1]
#	ans=ans+t[-1][1]
#	#if len(t)==1:
#	#	ans=t[0][1]
			
	fout.write('Case #'+str(i+1)+': '+str(ans)+'\n')
				
	

