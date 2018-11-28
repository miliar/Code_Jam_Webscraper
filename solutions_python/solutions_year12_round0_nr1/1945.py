#!/usr/bin/python3
import sys
Cases=[]
def translater(Googlerese):
	for i in Googlerese:
		letter=' '
		if(i=='a'):
			letter='y'
		if(i=='b'):
			letter='h'
		if(i=='c'):
			letter='e'
		if(i=='d'):
			letter='s'
		if(i=='e'):
			letter='o'
		if(i=='f'):
			letter='c'
		if(i=='g'):
			letter='v'
		if(i=='h'):
			letter='x'
		if(i=='i'):
			letter='d'
		if(i=='j'):
			letter='u'
		if(i=='k'):
			letter='i'
		if(i=='l'):
			letter='g'
		if(i=='m'):
			letter='l'
		if(i=='n'):
			letter='b'
		if(i=='o'):
			letter='k'
		if(i=='p'):
			letter='r'
		if(i=='q'):
			letter='z'
		if(i=='r'):
			letter='t'
		if(i=='s'):
			letter='n'
		if(i=='t'):
			letter='w'
		if(i=='u'):
			letter='j'
		if(i=='v'):
			letter='p'
		if(i=='w'):
			letter='f'
		if(i=='x'):
			letter='m'
		if(i=='y'):
			letter='a'
		if(i=='z'):
			letter='q'
		print(letter,end='')
try:
	with open(sys.argv[1],'r') as InputFile:
		CaseNumber=int(InputFile.readline())
		for i in range(0,CaseNumber):
			Cases.append(InputFile.readline())
except:
	sys.exit()
for i in range(0,CaseNumber):
	print("Case #"+str(i+1)+": ",end='')
	translater(Cases[i])
	print()
