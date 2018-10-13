import math
from decimal import *

def calcTime(C, F, X):
	C = Decimal(C)
	F = Decimal(F)
	X = Decimal(X)
	m = Decimal(math.ceil(((F*X)-(F*C)-(2*C))/(C*F)))
	if(m < 0): m = Decimal(0.000000)
	time = Decimal(0.00000000)
	for i in range(0, m):
		time += Decimal((C / (2 + F*i)))
	time += Decimal(X / (2 + (F*m)))
	if time == 1: time = Decimal(1.00000)
	return time

getcontext().prec = 10
fin = open('B-large.in')
lineCounter = 0
for line in fin:
	if(lineCounter == 0):
		pass
	else:
		aC = line.split(" ")[0]
		aF = line.split(" ")[1]
		aX = line.split(" ")[2]
		toPrint = str(Decimal(calcTime(aC, aF, aX)))
		if(toPrint == "1"): toPrint = "1.000000000"
		print "Case #"+str(lineCounter)+": " + toPrint
	lineCounter += 1
