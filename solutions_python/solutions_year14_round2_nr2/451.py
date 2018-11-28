import sys

filename = sys.argv[1]
f = open(filename, 'r')

numCases = int(f.readline())

for t in range(numCases):
	line = f.readline().strip().split(' ')
	A = int(line[0])
	B = int(line[1])
	K = int(line[2])

	pairs = []
	for a in range(A):
		for b in range(B):
			if (a&b < K):
				pairs.append((a,b))

	print 'Case #'+str(t+1)+': '+str(len(pairs))