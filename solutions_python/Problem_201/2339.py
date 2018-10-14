import sys
import collections

inputFile = open(sys.argv[1], "r") 
outputFile = open(sys.argv[2], "w") 
t = inputFile.readline()
for i in range(int(t)):

	numbers = inputFile.readline()
	n = numbers.split(" ")[0].strip()
	k = numbers.split(" ")[1].strip()
	maxN = 0
	min = 0
	gaps = collections.Counter()
	
	if( n == k ): 
		maxN = 0
		min = 0
	else:		
		for j in range(int(k)):
			if( len(gaps) == 0 ):
				maxN = int(n)
			else:
				maxN = max(list(gaps))
				
				gaps[maxN] -= 1
				if gaps[maxN] == 0 :
					del gaps[maxN]

			if maxN % 2 == 1 : 
				maxN = (maxN-1) / 2
				min = maxN
			else:
				maxN = maxN / 2
				min = maxN - 1
				
			gaps[maxN] += 1
			gaps[min] += 1
		
	outputFile.write('Case #'+ str(i+1) + ': ' + str(int(maxN)) + ' ' + str(int(min)) + '\n')

inputFile.close