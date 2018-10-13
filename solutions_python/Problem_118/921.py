#!/usr/bin/python

import sys
from math import sqrt,ceil,floor,log10

def isFair(n):
	orig=n
	rev=0
	while (n>0):
		dig=n%10
		rev=rev*10+dig
		n=n/10
	if orig==rev:
		return True

	return False

def nextPal(n):
	if (n==0):
		return 1
	dig=int(log10(n))+1
	if dig==1:
		res=n+1
		if res==10:
			return 11
		return res

	digitsBack=dig/2
	db=digitsBack
	divValue=10**digitsBack
	n/=divValue
	n=n+1
	#print "halved + 1="+str(n)
	#print "digits back="+str(db)

	remaining=n
	invert=0
	remainingDigits=int(log10(n))+1
	dPos=0
	while digitsBack>0:
		newDigit=remaining/(10**(remainingDigits-1))
		#print "New digit:"+str(newDigit)
		remaining=remaining%(10**(remainingDigits-1))
		invert=invert+(newDigit*(10**dPos))
		digitsBack=digitsBack-1
		remainingDigits=remainingDigits-1
		dPos=dPos+1
	n=n*(10**db)
	n=n+invert

	return n

def nextPalfromRegular(n):
	original=n
	if (n==0):
		return 1
	dig=int(log10(n))+1
	if dig==1:
		return n

	digitsBack=dig/2
	db=digitsBack
	divValue=10**digitsBack
	n/=divValue
	#print "halved + 1="+str(n)
	#print "digits back="+str(db)

	remaining=n
	invert=0
	remainingDigits=int(log10(n))+1
	dPos=0
	while digitsBack>0:
		newDigit=remaining/(10**(remainingDigits-1))
		#print "New digit:"+str(newDigit)
		remaining=remaining%(10**(remainingDigits-1))
		invert=invert+(newDigit*(10**dPos))
		digitsBack=digitsBack-1
		remainingDigits=remainingDigits-1
		dPos=dPos+1
	n=n*(10**db)
	n=n+invert

	if (n<original):
		return nextPal(original)

	return n	

def processCase(a,b):
	af=ceil(sqrt(float(a)))
	bf=floor(sqrt(float(b)))
	ai=int(af)
	bi=int(bf)
	total=0
	# *** BEGIN CODE PROCESSING CASE ***

	ai=nextPalfromRegular(ai)
	while ai<=bi:
		ii=ai*ai
		if isFair(ii):
			total=total+1
		ai=nextPal(ai)

	#for i in xrange(ai,bi+1):
		#nextPal(i)
	#	if isFair(i):
	#		ii=i*i
	#		if isFair(ii):
	#			total=total+1

	return str(total)

	# *** END CODE PROCESSING CASE ***

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
	a=caseInput.split()[0]
	b=caseInput.split()[1]

	# *** END CODE READING CASE ***

	solution=processCase(int(a),int(b))
	print "Case #"+str(case)+": "+solution

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

