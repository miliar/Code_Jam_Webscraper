# -*- coding: utf-8 -*-
INPUT  = ["A-small.in","A-large.in"]
OUTPUT = ["AllYourBase.out","AllYourBase-large.out"]
DEBUG  = 7
RUN    = 1

def dataImport(run):
	input = open(INPUT[run],"r")
	varT = int(input.readline()[:-1])
	return input,varT

def convertToTen(number,base):
	if ord(base) > 96:
		B = ord(base)-86
	else:
		B = ord(base)-48
	if B<2:
		B = 2
	inDecimal = 0
	for i in xrange(len(number)):
		decimal = number[i]
		if ord(decimal) > 96:
			X = ord(decimal)-86
		else:
			X = ord(decimal)-48
		inDecimal += X * (B**(len(number)-i-1))
	return inDecimal

def outputKase(number,output,varK):
	output.write("Case #"+str(int(varK+1))+": "+str(number)+'\n')
	output.flush()

def processKase(input,varK,output):
	number,base = processLine(input)
	#print int(varK+1),number,base
	outputKase(convertToTen(number,base),output,varK)

def processLine(input):
	line = input.readline()
	if '\n' in line:
		line = line.replace('\n','')
	dict = {}
	number = []
	dict[line[0]]='1'
	number.append("1")
	min = "0"
	char = 1
	while char < len(line):
		if line[char] in dict.keys():
			number.append(dict.get(line[char]))
		else:
			number.append(min)
			dict[line[char]]=min
			min = chr(ord(min)+1)
			if ord(min)==ord('1'):
				min = chr(ord(min)+1)
		char += 1
		
	return number, min


input,varT = dataImport(RUN)
output = open(OUTPUT[RUN],"w")
for K in xrange(varT):
	processKase(input,K,output)
output.close()