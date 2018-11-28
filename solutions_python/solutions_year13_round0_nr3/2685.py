#FairSquare.py
#John Ready 4/12/13
from __future__ import print_function, division
from math import sqrt, floor
import sys
import gmpy


#121  484  

def isSquare(n):
    return gmpy.is_square(n)

def isFair(num):
	return str(num) == str(num)[::-1]
	

def FairSquare(num):
	return (isSquare(num) and isFair(num) and isFair(int(sqrt(num))))

sys.stdout.softspace=0

def total(line):
	a,b = map(int, line.split(' '))
	counter = 0
	while a <= b:
		if FairSquare(a):
			counter += 1
		a += 1
	return counter
	

def readFile(myFile):
	f = open(myFile)
	
	i = 0
	for line in iter(f):
		if i==0:
			T = int(line)
		else:
			print("Case #"+str(i)+": " + str(total(line)),sep='')
		i +=1
		if i > T:
			break

readFile(sys.argv[1])
