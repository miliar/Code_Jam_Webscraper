#!/usr/bin/python

import sys

def extractQuiz(lines):
	answer1=int(lines[0].strip())
	answer2=int(lines[5].strip())
	arrange1=[]
	arrange2=[]
	for i in range(1,5):
		arrange1.append(lines[i].split())
		arrange2.append(lines[i+5].split())
	return (answer1,arrange1,answer2,arrange2)

def readFile(dir):
	f=open(dir)
	lines=f.readlines()
	T=int(lines[0].strip())
	rt=[]
	for i in range(T):
		#print lines[1+i*10:11+i*10]
		rt.append(extractQuiz(lines[1+i*10:11+i*10]))
	return rt

def sovleQuiz(quiz):
	row1=set(quiz[1][quiz[0]-1])
	row2=set(quiz[3][quiz[2]-1])
	card=row1.intersection(row2)
	#print quiz[1],quiz[0]
	if len(card)==1:
		return list(card)[0]
	elif len(card)>1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"

if __name__=="__main__":
	quizs=readFile(sys.argv[1])
	for i in range(len(quizs)):
		print("Case #%s: %s"%(i+1,sovleQuiz(quizs[i])))


