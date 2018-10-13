#!/usr/bin/python

import sys

#Main Part
for i in range(0,int(sys.stdin.readline().rstrip("\n"),10)):

#Input data
	line=sys.stdin.readline().rstrip("\n").split();
	SMax=int(line[0],10)
	SMax1=line[1]
	SDigits=[]
	friends=0

	for a in SMax1:
		SDigits.append(int(a,10))
	standup=SDigits[0]

	for z in range(1,SMax+1):

		if standup<z and SDigits[z]!=0:
			friends=friends+(z-standup)		
			standup=standup+(z-standup)+SDigits[z]
		else:
			standup=standup+SDigits[z]


# Solution
	#print(SMax,SMax1,SDigits)
		
		
# Results
	print("Case #"+str(i+1)+": "+str(friends))


