#!/usr/bin/python3
data=open("input")
output_file=open("output", "w")
n=data.readline()[0:-1]
testdata=data.readlines()
tt=0
for t in testdata:
		test=t[0:-1]
		stand=0
		add=0
		(s_max,pl)=test.split()
		ppl=[]
		for i in range(len(pl),0,-1):
				ppl.append(int(pl[len(pl)-i]))
		for i in range(0,len(ppl)):
				if(i>stand):
						while (stand<i):
								stand+=1
								add+=1
				stand+=ppl[i]
		tt+=1
		print("Case #"+str(tt)+": "+str(add),file=output_file)
