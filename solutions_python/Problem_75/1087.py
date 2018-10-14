#! /usr/bin/python 

from gcj_io import *
import re

def listToString(list):
	res='['
	if len(list) > 0:
		for i in list:
			res = res+i+', '
		res=res[0:-2]
	res=res+']'
	return res
	
				
def calcMagic(line):
	magic= re.split("\d",line)
	#print magic
	#print line
	#print magic
	invoke=magic[1].split()
	oppose=magic[2].split()
	formula=magic[-1].split()
	#print formula
	formula=formula[0]
	invokes={}
	opposes={}
	for string in invoke:
		invokes[string[0]+string[1]]=string[2]
	for string in oppose:
		opposes[string[0]]=string[1]
		opposes[string[1]]=string[0]
	#print invokes
	#print opposes
	#print invokes
	#print opposes
	spell=[]
	for char in formula:
		if spell != []:
			last = spell[-1]
			if invokes.has_key(char+last):
				spell[-1]=invokes[char+last]
				continue
			elif invokes.has_key(last+char):
				spell[-1]=invokes[last+char]
				continue
		if opposes.has_key(char):
			#if spell.find(opposes[char])!=-1:
			if opposes[char] in spell:
				spell=[]
				continue
		spell.append(char)
	return spell
	
	
	
input=startExercise()
case = int(input[1])
file = input[0]
output = openOutput()
for i in range(case):
	line=file.readline()
	res = listToString(calcMagic(line))
	writeCase(i,output,res)
    
finishExercise(file,output)
print "Problem resolved!"
