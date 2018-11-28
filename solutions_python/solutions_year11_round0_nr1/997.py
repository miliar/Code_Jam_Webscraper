import string

def getDataList():
	data = casetxt.split(" ")
	index = 0

	datalist = []

	noSteps = int(data[index])
	index = index +1 
	
	while(index<len(data)):
		if(data[index].upper()=="O"):
			index = index + 1
			datalist.append("O:"+str(int(data[index])))

		if(data[index].upper()=="B"):
			index = index + 1
			datalist.append("B:"+str(int(data[index])))

		index = index + 1

	return datalist

def findOtherRobot(list1,index):
	target = -1

	if(index+1<len(list1)-1 or index < 0):
		thisRobot = list1[index][0]

		if(thisRobot =="O"):
			otherRobot = "B"
		else:
			otherRobot = "O"

		for i in range(index,len(list1)):
			if(len(list1)>0):
				tmp = list1[i]
				if (tmp[0]==otherRobot):
					return i

	return target

def nextRobot(list1,index):
	target = -1
	if (index < 0):
		return -1
	if(index+1<=len(datalist)-1):
		thisRobot = list1[index][0]

		for i in range(index+1,len(list1)):
			if(len(list1)>0):
				tmp = list1[i]
				if (tmp[0]==thisRobot):
					return i
	return target

def getValue(list1, index):
	if(index <0):
		return -1
	else:
		data = list1[index]
	return int(data.split(":")[1])



def calculateTime(datalist):
	
	currentRobot = 0
	thisRobot = 0
	otherRobot = 0
	tstep = 1
	ostep = 1
	ttarget = 1
	otarget = 1
	time =0

	thisRobot = currentRobot
	otherRobot = findOtherRobot(datalist,thisRobot)
	
	while (currentRobot < len(datalist)):
		time = time + 1
		add =0
	
		if(thisRobot>-1):
			ttarget = getValue(datalist,thisRobot)
			
			if(ttarget > tstep):
				tstep = tstep +1 
			elif (ttarget < tstep):
				tstep = tstep -1 
			elif (ttarget == tstep):
				if(thisRobot== currentRobot):
					add = 1
					thisRobot = nextRobot(datalist,thisRobot)
			
		if(otherRobot>-1):
			otarget = getValue(datalist,otherRobot)
			
			if(otarget > ostep):
				ostep = ostep +1 
			elif (otarget < ostep):
				ostep = ostep -1 
			elif (otarget == ostep and add!=1):
				if(otherRobot== currentRobot):
					add = 1
					otherRobot = nextRobot(datalist,otherRobot)
					
		if(add ==1):
			currentRobot = currentRobot+1
			
	
		
	return time


infilename = "A-large.in"
outfilename = "A_large.out"

f = open(infilename,"r")
o = open(outfilename,"w")
cases = int(f.readline())
case =0
datalist = []

for casetxt in f:
	case = case +1
	datalist = getDataList()
	o.write("Case #"+str(case)+": "+str(calculateTime(datalist))+"\n")



