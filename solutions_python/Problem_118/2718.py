#!/bin/bash

def isPalindrome(number):
	numString = str(number)

	if numString != numString[::-1]:
		return False

	return True

def findMinimumSquare(value):
	while True:
		number = value**0.5

		numberInt = int(number)

		if numberInt == number:
			return numberInt

		value += 1

def process(a, b):
	count = 0

	number = findMinimumSquare(a)
	
	while True:
		if isPalindrome(number):
			result = number**2

			if result > b:
				break

			if isPalindrome(result):
				count += 1

		number += 1

	return count

with open('fair_and_square_test.txt', 'r') as f:
	numCases = 0
	
	for i, line in enumerate(f):
		line = line.strip()
		optionsList = line.split(' ')

		if i == 0:
			numCases = int(line)
		else:
			a = int(optionsList[0])
			b = int(optionsList[1])

			value = process(a, b)
			print "Case #%d: %d" % (i, value)

		if i == numCases:
			break;
