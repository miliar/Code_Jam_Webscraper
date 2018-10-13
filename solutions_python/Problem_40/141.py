#!/usr/bin/env python 

import sys 
import re 
from decimal import *



class node:
	def __init__(self,value):
		self.__child = {}
		self.__value = value 
		


	def setChild(self,node,name):
		self.__child[name] = node

	
	def getChild(self):
		return(self.__child)


	def getValue(self):
		return(self.__value)


	def getname(self):
		return(self.__name)
	
def readTree():
	nLines = int(sys.stdin.readline())

	Stack1 = []
	Stack2 = []   # for node 
	
	Stack1.append("root")
	line = ""
	for i in range(nLines):
		line += sys.stdin.readline().strip()

	line = line.strip()
	#print line 

	string = ""	
	ch = 0
	while(ch < len(line)):
		#print ch 
		while(ch < len(line) and line[ch]!= '(' and line[ch] != ')'):
			string += line[ch]
			ch += 1
			
		#print string
		#print line[ch]
		
		if(string.strip()):
			Stack1.append(string)
			string = ""
		
		#print Stack1 
		
		if(ch < len(line) and line[ch] == ')'):
			ch += 1
			#Str = string
			#print Stack1 
			Str = Stack1.pop().strip()
			#print Stack1 
			#print "----" , Str
			field = Str.split(' ')
			if(len(field) > 1):
				# non leaf node 
				newNode = node(field[0])
				child1 = Stack2.pop()
				child2 = Stack2.pop()

				newNode.setChild(child2,field[1])
				newNode.setChild(child1,"other")
				Stack2.append(newNode)

			else:
				newNode = node(field[0])	 
				Stack2.append(newNode)



		if(ch < len(line) and line[ch] == '('):
				#Stack1.append(string)
				string = ""
				ch += 1
				
				
	return(Stack2[0])
	#print Stack1 			
	#print Stack2 
				
			


def findProb(Root,feat):
	Prob = 1.0000000
	root = Root 
	while(True):
		Prob *= float(root.getValue())
		child = (root.getChild())
		#print child 
		if(len(child) == 0):
			break
	
		else:
			flag = 0
			for key in child.keys():
				if(key in feat):
					root = child[key]
					flag = 1
					#print key 
					break
			if(flag == 0):
				#print 'other'
				root = child['other']
				
	return( Prob )



def process():
	Root = readTree()

	#print Root.getValue()

	nTests = int(sys.stdin.readline().strip())
	for i in range(nTests):
		line = sys.stdin.readline().strip().split(' ')
		features = line[2:]
		#print features
		prob = findProb(Root,features)	
		print "%.7f"  % prob
		#print prob


					
	

if(__name__=="__main__"):
	getcontext().prec = 7

	nTestCases = int(sys.stdin.readline().strip())
	#nTestCases = 1
	for i in range(1,nTestCases+1):
		print "Case #" + str(i) + ":"
		process()
	
