#!/bin/usr/python

def checkNumber(tmpNumber):
	tmpDigit = 10
	digit = 1

	while tmpNumber >= 10:
		if tmpNumber % 10 < tmpNumber / 10 % 10:
			return False, digit
		elif tmpNumber % 10 == tmpNumber / 10 % 10:
			tmpDigit *= 10
		else:
			digit *= tmpDigit
			tmpDigit = 10
		tmpNumber /= 10
	return True, 0

def resolveTidyNumberProblem(number):
	while 42:
		tmpNumber = number
		while tmpNumber != 0:
			result, digit = checkNumber(tmpNumber)
			if result != True:
				while digit > 0:
					if digit != 1:
						tmpNumber -= (tmpNumber	/ digit % 10) * digit
					else:
						tmpNumber -= (tmpNumber	/ digit % 10 + 1) * digit
					digit /= 10
			else:
				break
		if (tmpNumber != 0):
			return tmpNumber

nbTest = input()
for i in range(1, nbTest + 1):
	number = input()
	number = resolveTidyNumberProblem(number)
	print "Case #"+ str(i) + ":", number