from __future__ import print_function

def killLeadingZeros(num):
	firstSignificant = 0
	for i in range(0,len(num)):
		if num[i] != 0:
			firstSignificant = i
			break
	
	return num[firstSignificant:]
			

def isTidy(num):
	flag = True
	place = -1
	
	for i in range(1,len(num)):
		if  not (num[i-1] <= num[i]):
			flag = False
			place = i-1 #place where the fault is found
			break #if this doesnt work, I can return here
	
	#breaking out of the for if we found the first inconsistency
	return(flag,place)

def fixUp(num,place):
	#decrement the conflicting value and change the subsequent to 9s
	num[place] = num[place] - 1
	
	for i in range(place+1,len(num)):
		num[i] = 9


def lastTidyNumber(s):
	num = [int(s[0])] #start the list with the first digit of the number
	#iterate through the next digits and concatenate them to the list.
	for i in range(1,len(s)):
		num = num + [int(s[i])]
	
	#num now holds the list of digits.
	tidyFlag = False
	
	(tidyFlag,place) = isTidy(num)
	
	while not tidyFlag:
		fixUp(num,place)
		(tidyFlag,place) = isTidy(num)
	
	#num is tidy now but can have leading zeros
	num = killLeadingZeros(num)
	
	
	#num should be the tidy answer, we'll convert it to a flat string
	
	ans = str(num[0])
	for i in range(1,len(num)):
		ans = ans + str(num[i])
	
	return ans



#---------- Start of 'main' stuff
T = int(raw_input())

#range is [) as expected
for i in range(0,T):
	s = raw_input() #We get the string that represents the number
	print ("Case #" + str(i+1) + ": " + lastTidyNumber(s)) #+ str(FUNCTIONGOESHERE)
	
