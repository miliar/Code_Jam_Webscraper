import os
import math
def WriteFile(b,a):
	f= open(a,"w+")
	for line in b:
		f.write(line+"\n")
	f.close

def ReadFile(a):
	return([line.rstrip('\n') for line in open(a)])


def FindStall(ListOfStalls,cord):
	i=cord
	Left = 0
	while not(ListOfStalls[i]):
		Left+=1
		i-=1
	
	i=cord
	Right = 0
	while not(ListOfStalls[i]):
		Right+=1
		i+=1
	return(Left,Right)
 
def make_case(d):
	for i in range(len(d)):
		d[i] = "Case #" + str(i+1) + ": " + d[i]
	return(d)
	

FileIn = 'C-small-1-attempt1.in'
lines = ReadFile(FileIn)
del lines[0]
l=[]
def maincode():
	for line in lines:
		NumberOfStalls,People = line.split(' ', 1)
		NumberOfStalls = int(NumberOfStalls)+2
		People = int(People)
		StallList = [False] * NumberOfStalls
		StallList[0] = True
		StallList[-1] = True
		for p in range(People):
			BestPos=0
			a=0
			for i in range(0,len(StallList)-1):
				Left,Right = FindStall(StallList,i)
				if a < Left*Right:
					a = Left*Right
					BestPos = i
			StallList[BestPos] = True
			
		StallList[BestPos] = False
		Left,Right = FindStall(StallList,BestPos)
		l.append(str(max(Right,Left)-1) + " " + str(min(Right,Left)-1))
		#os.system("pause")
maincode()
print(l)
l = make_case(l)
WriteFile(l,'C-small-1-attempt1.out')
