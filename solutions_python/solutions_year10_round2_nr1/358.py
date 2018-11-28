#!/usr/bin/python
#  Developed by Rajiv Poplai 
import sys
#import pdb
#pdb.set_trace()



def main():
	fileName = sys.argv[1]

	# Open input and output files
	inputFile = open(fileName, 'r')
	outputFile = open(fileName.strip('.in')+'.out', 'w')

	testCases = int(inputFile.readline().strip())
	
	for i in xrange(testCases):
		dirMap = []
		(N, M) = map(int, inputFile.readline().strip().split())
		for j in xrange(N):
			arr = inputFile.readline().strip().split('/')
			del arr[0]
			substr = ''
			for k in xrange(len(arr)):
				substr=''.join([substr, '/', arr[k]])
				if not substr in dirMap:
					dirMap.append(substr) 
		count = 0
		for j in xrange(M):
			arr = inputFile.readline().strip().split('/')
			del arr[0]
			substr = ''
			for k in xrange(len(arr)):
				substr=''.join([substr, '/', arr[k]])
				if not substr in dirMap:
					dirMap.append(substr)		
					count = count + 1
		outputFile.write('Case #'+str(i+1)+': '+str(count) + '\n')

	# Close input and output files
	inputFile.close()
	outputFile.close()

if __name__ == "__main__":
	main()
