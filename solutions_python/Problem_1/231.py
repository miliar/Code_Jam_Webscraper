#! /usr/bin/env python
f=open('A-large.in', 'r')
f2=open('A-large.out','w')
intQNumber=int(f.readline())
for intLoopCount in range(intQNumber):
	intDictSize=int(f.readline())
	dicSearch={}
	for intCount in range(intDictSize):
		a=f.readline()
		a=a[:-1]
		dicSearch[a]=intCount
	intQueryNum=int(f.readline())
	lstCheck=range(intDictSize)
	for intCount in range(intDictSize):
		lstCheck[intCount]=0
	intSetUnique=0
	intSwitchCount=0
	for intCount in range(intQueryNum):
	        a=f.readline()
	        a=a[:-1]
		if lstCheck[dicSearch[a]]==0:
			intSetUnique+=1
			if intSetUnique==intDictSize:
				intSwitchCount+=1
				for intCount in range(intDictSize):
				        lstCheck[intCount]=0
				intSetUnique=1
	                lstCheck[dicSearch[a]]=1
	f2.write('Case #'+str(intLoopCount+1)+': '+str(intSwitchCount)+'\n')
f.close()
f2.close()
