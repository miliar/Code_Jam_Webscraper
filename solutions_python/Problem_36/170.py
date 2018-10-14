# -*- coding: utf-8 -*-
INPUT = ["C-small.in","C-large.in"]
OUTPUT = ["Welcome-small.out","Welcome-large.out"]
RUN = 1
welcome = ["w","e","l","c","o","m","1"," ","t","3","7","5","4","d","2","8","j","a","6"]
#s = "wweellccoommee to code qps jam"
conversion = {'e':'1','1':'2','o':'3','3':'4','c':'5','m':'6',' ':'7','7':'8'}
conversion_index={2:'e',7:'1',5:'o',10:'3',4:'c',6:'m',8:' ',11:'7'}
DEBUG = 0

def getInput(run):
	input = open(INPUT[run],"r")
	var_N = int(input.readline()[:-1])
	return input,var_N

def initiateLineInt(line,line_int):
	start = 0
	while True:
		index = line.find(welcome[0],start)
		if index == -1:
			break
		line_int[index]=1
		start=index+1

def outputData(output,total,var_K):
	total_str=str(total)
	output.write("Case #"+str(var_K+1)+": "+"0"*(4-len(total_str))+total_str+"\n")
	output.flush()

def processLine(line,var_K,output):
	line_int = []
	for c in xrange(len(line)):
		line_int.append(0)
	start = 0
	initiateLineInt(line,line_int)
	pos = 0
	while pos < len(welcome):
		start = 0
		while True:
			index = line.find(welcome[pos],start)
			if index==-1:
				break
			start2 = 0
			while True:
				index2 = line.find(welcome[pos-1],start2,index)
				if index2==-1:
					break
				line_int[index]=(line_int[index]+line_int[index2])%10000
				start2 = index2+1
			start = index+1
		if pos in conversion_index.keys():
			while True:
				index = line.find(conversion_index.get(pos))
				if index==-1:
					break
				line=line[:index]+str(conversion.get(conversion_index.get(pos)))+line[index+1:]
				line_int[index]=0
		pos+=1
	outputData(output,processTotal(line,line_int),var_K)

def processTotal(line,line_int):
	start = 0
	total = 0
	while True:
		index = line.find(welcome[-1],start)
		if index==-1:
			break
		total=(total+line_int[index])%10000
		start = index+1
	return total


input,var_N = getInput(RUN)
output = open (OUTPUT[RUN],"w")

for i in xrange(var_N):
	processLine(input.readline()[:-1],i,output)
