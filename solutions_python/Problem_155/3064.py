#!/usr/bin/env python

def readFile(fileName):
	f = open(fileName)
	N = int(f.readline().strip())
	data= []
	for i in range(N):
		datum = f.readline().strip().split()
		mostShy = int(datum[0])
		allShy = [int(x) for x in list(datum[1])]
		data.append( (mostShy,allShy) )
	return data

def output(data):
	for i,datum in enumerate(data):
		print "Case #"+str(i+1)+": "+str(datum)

def main(fileName):
	data = readFile(fileName)

	solutions = []
	for datum in data:
		clapCount = 0
		addedPeeps = 0
		for shyLevel,people in enumerate(datum[1]):
			while clapCount < shyLevel:
				addedPeeps += 1
				clapCount += 1
			clapCount += people
		solutions.append(addedPeeps)
	output(solutions)
				



if __name__ == "__main__":
	from sys import argv
	main(argv[1])
