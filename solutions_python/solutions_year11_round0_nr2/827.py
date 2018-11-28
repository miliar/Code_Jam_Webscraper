#!/usr/bin/python

def main():

	#handle input
	#input format
	#C number of strings
	#[C] string containing three letters, two base followed by non base
	#[D] string containing two characters... two base characters that are opposed 
	#[N] series of base elements you are to invoke, left to right.
	#T // T testcases
	#C [C] D [D] N [N]
	outlist = list()
	numberOfTestCases = int(raw_input())
	for case in range(1, numberOfTestCases + 1):
		
		###### Handle Input Start	
		caseString = raw_input().split(" ")
		#handle C // Combo Sets
		numOfCombos = int(caseString.pop(0))
		comboList = list()
		if( numOfCombos != 0 ):
			for each in range(numOfCombos):
				comboList.append(caseString.pop(0))
		#handle D // Oppose Sets
		numOfOppose = int(caseString.pop(0))
		opposeList = list()
		if (numOfOppose != 0):
			for each in range(numOfOppose):
				opposeList.append(caseString.pop(0))
		#handle N // elementSeries
		numElements = int(caseString.pop(0))
		elementList = list(caseString[0])
		###### Handle Input End
		
		outputElementList = list()
		outputElementList.append(elementList.pop(0))
		while(len(elementList) != 0):
			if (len(outputElementList) == 0):
				outputElementList.append(elementList.pop(0))
			else:
				outputElementList.append(elementList.pop(0))
				match = False
				for characterCombo in comboList:
					if ( isCombo(characterCombo[0], characterCombo[1], outputElementList[-2:])):
						outputElementList.pop(-1)
						outputElementList.pop(-1)
						outputElementList.append(characterCombo[2])
						match = True
						break
				if (match == False):
						for charCombo in opposeList:
							if ( isOpposed(charCombo[0], charCombo[1], outputElementList) ):
								outputElementList = list()
								break
		outlist.append(outputElementList)
	count = 1
	for each in outlist:
		output(count, each)
		count += 1
def output(numCase, elementList):
	outstring = "["	
	for each in elementList:
		outstring += str(each) + ", "
	if (len(elementList) != 0):
		outstring = outstring[:-2]
	outstring += "]"
	print "Case #" + str(numCase) + ": " + outstring			
def isOpposed(char1, char2, elementList):
	char1T = False
	char2T = False
	for each in elementList:
		if ( each == char1 ):
			char1T = True
		if ( each == char2 ):
			char2T = True
	if ( (char1T == True) and (char2T == True) ):
		return True
	else:
		return False

def isCombo(char1, char2, elementList):
	if ( (elementList[-1] == char1) and (elementList[-2] == char2)):
		return True
	if ( (elementList[-1] == char2) and (elementList[-2] == char1)):
		return True
	return False
		
	
		
main()
