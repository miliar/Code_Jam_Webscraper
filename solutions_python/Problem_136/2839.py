import os
import sys


def solveTestCase(testCase):
	params=testCase.split()
	C=float(params[0])
	F=float(params[1])
	X=float(params[2])	
	
	totalTime=0.0
	Fx=2.0
	Fy=2.0+F
	Ttx=X/Fx
	Tf=C/Fx
	Tty=X/Fy
	while Ttx>(Tf+Tty):
		totalTime+=Tf
		Fx=Fy
		Fy+=F
		Ttx=X/Fx
		Tf=C/Fx
		Tty=X/Fy
		
	totalTime+=Ttx	

	return totalTime

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
	for currentCase in xrange(1, numberOfTests+1):
		outputFile.write('Case #'+str(currentCase)+': '+str(solveTestCase(testCases[currentCase]))+'\n')

	
	outputFile.close()

if __name__ == '__main__':
	main()
