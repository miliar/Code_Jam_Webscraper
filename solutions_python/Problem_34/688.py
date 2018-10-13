#!/usr/bin/python

rawInput = raw_input()
L = int(rawInput.split(" ")[0])
D = int(rawInput.split(" ")[1])
N = int(rawInput.split(" ")[2])

dictionary = []
chkInput = []
finalResult = []
finalIndex = 0
inOrOut = 0
count = 0

for i in range(0,D):
	dictionary.append(raw_input().split('\n')[0])

for i in range(0,N):
	chkInput.append(raw_input().split('\n')[0])
	

#----------------------- PARSING

eachInput = []
temp = []
for each in chkInput:
	eachInput = []
	temp = []
	for idea in range(0,len(each)):
		if each[idea]=='(':
			inOrOut = 1
		elif each[idea]==')':
			if len(temp)!=0:
				eachInput.append(temp)
				temp=[]
			inOrOut = 0
		else:
			if inOrOut == 0:
				eachInput.append(each[idea])
			else:
				temp.append(each[idea])
		
	
#----------------------- CHECKING
	index = 0
	count = 0
	flag = -1
		
	for word in dictionary:
		for index in range(0,L):
			if eachInput[index].__contains__(word[index]):
				flag = -1
			else:	
				flag = 0; break
		if flag == -1:
			count+=1
		
	finalResult.append(count)
				
for i in range(0,len(finalResult)):
	print "Case #"+str(i+1)+": "+str(finalResult[i])
	


"""		if eachInput[index].__contains__(word[index]):
			print yup
		else:
			flag = 0
			break
		if index < L:
			index+=1
		else:
			index=0
	if flag == -1:
		finalResult[finalIndex]+=1
	finalIndex+=1

print finalResult	"""
