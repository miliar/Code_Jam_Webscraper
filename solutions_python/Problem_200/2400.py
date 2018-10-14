#!/usr/bin/env python3

import string

caseNr=int(input("Input:  "))

testCases =[]
output = []
correct = True;

for i in range(caseNr):
	testCases.append(input(""))


for case in testCases:
	number = case
	while True:
		correct = True
		temp = []
		for i in range(len(number)-1):
			if(number[i]>number[i+1]):
				correct = False
				val = int(number[i])-1
				temp.append(str(val))
				for j in range(len(number)-i-1):
					temp.append("9")
				break
			else:
				temp.append(number[i])
		if correct:
			break
		number = "".join(temp)

	output.append(int(number))

for out in range(len(output)):
	print ("Case #"+str(out+1)+": "+str(output[out]))
		
