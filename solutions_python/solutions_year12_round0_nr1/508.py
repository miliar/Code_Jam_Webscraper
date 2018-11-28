#!/usr/bin/python

import sys
import string

ttable=string.maketrans("zyeq ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv","qaoz our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up")

def processCase(case,caseInput):
	# *** BEGIN CODE PROCESSING CASE ***

	cad=string.translate(caseInput,ttable)

	# *** END CODE PROCESSING CASE ***
	return cad 

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
		
	# *** END CODE READING CASE ***

	solution=processCase(case,caseInput)
	print "Case #"+str(case)+": "+solution.rstrip()

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

