import sys

f = open(sys.argv[1])
T = int(f.readline())

def readInts():
	return list(map(int, f.readline().strip().split(' ')))

for t in range(T):
	ints = readInts()
	A = ints[0]
	B = ints[1]
	K = ints[2]
	
	count = 0
	for a in range(A):
		for b in range(B):
			if a & b < K:
				count += 1
	
	
	print 'Case #%d:' % (t + 1), count
