#!/usr/bin/python3
import sys
Cases=[]
def googler(Case):
	numbers=[]
	Data=Case.split(' ')
	for i in Data:
		numbers.append(int(i))
	N=numbers.pop(0)
	S=numbers.pop(0)
	p=numbers.pop(0)
	count=0
	more=0
	for i in numbers:
		if(i>p*3-3):
			count+=1
		elif(i>p*3-5 and i>1):
			more+=1
	if(more<=S):				
		print(count+more)
	elif(more>S):
		print(count+S)
try:
	with open(sys.argv[1],'r') as InputFile:
		CaseNumber=int(InputFile.readline())
		for i in range(0,CaseNumber):
			Cases.append(InputFile.readline())
except:
	sys.exit()
for i in range(0,CaseNumber):
	print("Case #"+str(i+1)+": ",end='')
	(Case,line_feed)=Cases[i].split('\n')
	googler(Case)
