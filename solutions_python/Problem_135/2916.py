import os
import sys
from sets import Set

def solveTestCase(testCases, testCaseStartIndex):
	rowNumber1=int(testCases[testCaseStartIndex])
	cardsInRow1=parseCardRow(testCases[testCaseStartIndex+rowNumber1])
	rowNumber2=int(testCases[testCaseStartIndex+5])
	cardsInRow2=parseCardRow(testCases[testCaseStartIndex+5+rowNumber2])
	resultingCard=cardsInRow1.intersection(cardsInRow2)
	
	numberOfCards=len(resultingCard)
	if numberOfCards==1:
		return resultingCard.pop()
	elif numberOfCards==0:
		return 'Volunteer cheated!'
	else:
		return 'Bad magician!'

def parseCardRow(cardsInRow):
	cards= cardsInRow.split()	
	cardSet=Set([cards[0],cards[1],cards[2],cards[3]])
	return cardSet

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] ' + filename + ' does not exist'
			exit(-1)
		if not os.access(filename, os.R_OK):
			print '[-] ' + filename + 'access denied.'
			exit(-1)
	else :
		print '[-] Usage: ' + str(sys.argv[0]) + ' <filename>'
		exit(-1)
	
	inputFile = open(filename, 'r')
	outputFile = open('output', 'w')
	
	testCases = inputFile.readlines()
	numberOfTests = int(testCases[0])
	testCaseStartIndex=1
	for currentCase in xrange(1, numberOfTests+1):
		outputFile.write('Case #'+str(currentCase)+': '+str(solveTestCase(testCases, testCaseStartIndex))+'\n')
		testCaseStartIndex+=10
	
	outputFile.close()

if __name__ == '__main__':
	main()
