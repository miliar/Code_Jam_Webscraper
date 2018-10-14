import sys
import math

def genTrees(x, y, n, A, B, C, D, M):
	trees = []
	trees.append([x, y])
	X = x
	Y = y
	for i in range(1, n):
		X = int(math.fmod((A * X + B), M))
		Y = int(math.fmod((C * Y + D), M))
		trees.append([X, Y])
	return trees
	
def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
				
def calcMiddle(tri):
	X = float(tri[0][0] + tri[1][0] + tri[2][0])/3.0
	Y = float(tri[0][1] + tri[1][1] + tri[2][1])/3.0
	return math.modf(X)[0], math.modf(Y)[0]


outfile = open("tri.txt", "w")
infile = open("A-small-attempt0.in", "r")

num_cases = int(infile.readline())

for i in range(1, num_cases + 1):
	triangles = 0
	line = infile.readline()
	temp = line.split()
	n = int(temp[0])
	A = int(temp[1])
	B = int(temp[2])
	C = int(temp[3])
	D = int(temp[4])
	x = int(temp[5])
	y = int(temp[6])
	M = int(temp[7])
	trees = genTrees(x, y, n, A, B, C, D, M)
	combine = xuniqueCombinations(trees, 3)
	for arr in combine:
		X, Y = calcMiddle(arr)
		if X == 0 and Y == 0:
			triangles = triangles + 1
			
	outfile.write("Case #%s: %s\n" % (i, triangles))
infile.close()
outfile.close()