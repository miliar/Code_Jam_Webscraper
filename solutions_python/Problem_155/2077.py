import sys
from collections import defaultdict
import re

""" Read the input file """
def  readFile():
	inputFile=open(sys.argv[1],'r')
	allLines=inputFile.readlines()
	outputFile=open('output.txt','w')

	#Intializing number of cases
	no_of_cases=int(allLines[0])	
	#store the input in the way required to do 
	return no_of_cases,allLines,outputFile


no_of_cases,input_cases,outputFile=readFile()

count=1
while count<=no_of_cases:
	#print "no_of_cases:",no_of_cases
	array1=input_cases[count].split(' ')
	#print "array1:",array1
	maxSi=int(array1[0])
	#print "maxSi",maxSi
	i=1
	totalPeople=int(array1[1][0])
	#print "totalPeople:",totalPeople
	addedPeople=0
	need=0
	while i<=maxSi:
		#print "Now Comparing totalPeople:",totalPeople," Comparing With:",int(array1[1][i])
		#print "TotalPeople:",totalPeople
		#print "NextSi:",i
		#print "Next People:",array1[1][i]
		if int(array1[1][i])!=0:
			if totalPeople>i:
				totalPeople=int(totalPeople)+int(array1[1][i])
			if totalPeople<=i:			
				need=i-int (totalPeople)
				if need!=0:
					#print "need:",need						
					addedPeople=addedPeople+need
				totalPeople=totalPeople+int(array1[1][i])+need
		i=i+1	
		#print "added People Now:",need
		#print "updated totalPeople:",totalPeople
	#print "added People:",addedPeople
	#print "Case #"+str(count)+":"+" "+str(addedPeople)
	#raw_input()
	outputFile.write("Case #"+str(count)+":"+" "+str(addedPeople))
	outputFile.write("\n")
	count=count+1		
		
		

