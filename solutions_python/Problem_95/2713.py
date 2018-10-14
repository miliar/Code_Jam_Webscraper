#!/usr/bin/python
import sys
import string

def printOutput(string, case):
	print "Case #"+str(case)+": "+string

trainfile = open('train.txt')
trainfile_list = map(str.strip, trainfile.readlines())
size = len(trainfile_list)/2
org_list=str()
google_lang=str()
for i in range(0,size):
	org_list += trainfile_list[2*i]
	google_lang += trainfile_list[2*i+1]
	
tran_str = string.maketrans(google_lang,org_list)
actual = sys.stdin
actual_list = map( str.strip, actual.readlines() )
translated =map( lambda x: str.translate(x, tran_str) , actual_list )
for i in range(1,len(translated)):
	printOutput(translated[i],i)
