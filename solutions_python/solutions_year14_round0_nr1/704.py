# MagicTrick.py
"""
date: 2014-04-12
description: A program solving the 2014 Google Code Jam Problem A.
"""
import string

def readfile(filename):
	fInput = open(filename, 'r')
	lstCases = []
	SIZE = 4

	caseNum = int(fInput.readline())
	#lines = fInput.read().split()

	for case in range(0, caseNum):
		lstMatrix = []
		for rnd in range(0, 2):
			rowNum = int(fInput.readline())
			line = []
			for index in range(0, SIZE):
				if index == rowNum - 1: 
					line = string.replace(fInput.readline(), '\n', '').split(' ')
				else:
					fInput.readline()
			lstMatrix.append(line)
		lstCases.append(lstMatrix)

	print lstCases
	return lstCases

def process(lstCases):
	cnCase = 0
	fOutput = open('A-small-attempt0.out', 'w')

	for lstMatrix in lstCases:
		cnCase += 1
		first, second = lstMatrix[0], lstMatrix[1]

		counter = 0
		for f in first:
			if f in second:
				counter += 1
				result = f

		fOutput.write('Case #'+str(cnCase)+': ' )
		if counter == 0:
			fOutput.write('Volunteer cheated!\n')
		elif counter == 1:
			fOutput.write(result+'\n')
		else:
			fOutput.write('Bad magician!\n')

	fOutput.close()

def main():
	filename = 'A-small-attempt0.in'
	process(readfile(filename))

if __name__ == '__main__':
	main()

