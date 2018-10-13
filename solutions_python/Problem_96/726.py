#!/usr/bin/python

import sys

val={}
for i in range(0,31):
	val[i]=[]	

for i in range(0,11):
	for j in range(0,11):
		for z in range(0,11):
			val[i+j+z].append([i,j,z])


if 1==1:#sys.stdin.readline().rstrip("\n")=='Input':
	count = int(sys.stdin.readline(),10)
	#sys.stdout.write("Output\n")
	for i in range(0,count):
		line=sys.stdin.readline().rstrip("\n")
		in_=line.split()
		p=int(in_[2],10)
		s=int(in_[1],10)
		n=int(in_[0],10)
		m_s = 0
		m_h = 0
		m_result=[]
		for j in range(0,n):
			how=0
			sup=0

			for ss in val[int(in_[j+3],10)]:

				if abs(ss[0]-ss[1])<3 and abs(ss[1]-ss[2])<3 and abs(ss[2]-ss[0])<3 and (ss[0]>=p or ss[1]>=p or ss[2]>=p):
					if abs(ss[0]-ss[1])==2 or abs(ss[1]-ss[2])==2 or abs(ss[2]-ss[0])==2:
						sup=sup+1
					else:
						how=how+1
			if sup>0 and how<=0:
				m_s =m_s+1
			if how>0 or sup>0:
				m_h =m_h+1
		
		r=0
		if m_s<=s:	
			r=m_h
		else:
			r=m_h-abs(m_s-s)
		sys.stdout.write("Case #"+str(i+1)+": "+str(r)+"\n")
