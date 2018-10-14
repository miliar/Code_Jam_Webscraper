#!/usr/bin/env python3

caseNr=int(input("Input:  "))

testCases= []
output =[]

for i in range(caseNr):
	testCases.append(input(""))

for case in testCases:
	temp = case.split(" ")
	states = list(temp[0])
	K = int(temp[1])
	
	count = 0
	for i in range(len(states)):
		if states[i] == '-': 
			if i < len(states)-K+1:
				for j in range(K):
					if states[i+j] == '-':
						states[i+j]='+'
					else:
						states[i+j]='-'
				count += 1
			else:
				count = "IMPOSSIBLE"
				break
		
	output.append(count)

for out in range(len(output)):
	print ("Case #"+str(out+1)+": "+str(output[out]))

				
