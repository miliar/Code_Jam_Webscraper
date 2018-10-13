#!bin/python

import sys

def main(input):

	f = open(input[0],'r')
	f2 = open(input[0][:input[0].index(".")]+".out", 'w')
	lines = []
	for l in f:
		lines += [l]	
	
	numCases = int( lines[0].strip() )

	cases = []
	for i in range(numCases):
		f2.write("Case #" + str(i+1)+ ": ")

		answerOne = int(lines[i*10+1].strip())
		rowData = [ int(x.strip()) for x in lines[i*10+1+answerOne].split(" ") ]
		answerTwo = int(lines[i*10+6].strip())
		rowDataTwo = [ int(x.strip()) for x in lines[i*10+6+answerTwo].split(" ") ]

		print rowData
		print rowDataTwo
		possibleCount = 0
		answer = None
		for cardOne in rowData:
			if cardOne in rowDataTwo:
				possibleCount += 1	
				answer = cardOne
		
		if possibleCount == 0:
			f2.write("Volunteer cheated!\n")
		elif possibleCount == 1:
			f2.write(str(answer) + "\n")
		else:
			f2.write("Bad magician!\n")

	

if __name__ == "__main__":
   main(sys.argv[1:])
