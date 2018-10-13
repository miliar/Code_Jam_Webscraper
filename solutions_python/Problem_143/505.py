import sys

file = sys.argv[1]

lines = open(file).readlines()
T = int(lines[0])

currentLine = 1

for case in range(T):
	A,B,K = map(int,lines[currentLine].split())
	currentLine = currentLine + 1

	totalCount = 0
	for A1 in range(A):
		for B1 in range(B):
			if A1 & B1 < K:
				totalCount +=1		
						
	print "Case #{}: {}".format(case + 1 ,totalCount )