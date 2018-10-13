from __future__ import with_statement
from math import *

def bucketToXY(bucket):
	return (bucket % 3, (bucket / 3) % 3)

def compatible(b1, b2, b3):
	b1x, b1y = bucketToXY(b1)
	b2x, b2y = bucketToXY(b2)
	b3x, b3y = bucketToXY(b3)
	return ((b1x + b2x + b3x) % 3 == 0) and ((b1y + b2y + b3y) % 3 == 0) 
	
def processFile(fin, outf):
	numCases = int(fin.readline())
	for caseNumber in xrange(1, numCases + 1):
		n, A, B, C, D, x, y, M = map(int, fin.readline().strip().split())
		
		buckets = [0 for i in range(9)]

		for i in range(n):
			#print x, y
			buckets[(x % 3) * 3 + y % 3] += 1
			x = (A * x + B) % M
			y = (C * y + D) % M
		
		res = 0
		
		for b1 in range(9):
			for b2 in range(b1, 9):
				for b3 in range(b2, 9):
					if compatible(b1, b2, b3):
						n1 = buckets[b1]
						n2 = buckets[b2]
						n3 = buckets[b3]
						if n1 == 0 or n2 == 0 or n3 == 0:
							continue
						
						if b1 == b2 and b2 == b3:
							if (n1 >= 3):
								res += n1 * (n1 - 1) * (n1 - 2) / 6
						else:
							combDivisor = 1
							if b1 == b2:
								n2 -= 1
								combDivisor = 2
							if b1 == b3:
								n3 -= 1
								combDivisor = 2
							if b2 == b3:
								n3 -= 1
								combDivisor = 2
							res += n1 * n2 * n3 / combDivisor
						
		
		s = "Case #" + str(caseNumber) + ": " + str(res)
		print s
		print >> outf, s



input = "A-large"
with open(input + ".in") as f:
	with open(input + ".out", "w") as fout:
		processFile(f, fout)
print "OK!"