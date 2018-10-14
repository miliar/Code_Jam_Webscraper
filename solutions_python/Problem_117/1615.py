import fileinput
import sys


def isLawnPossible(lawn,n,m):
	for x in range(0,n):
		for y in range(0,m):
			square=lawn[x][y]
			across=False
			down=False
			for l in range(0,m):
				if lawn[x][l] > square:
					across=True
					break
			for u in range(0,n):
				if lawn[u][y] > square:
					down=True
					break
			if across and down:
				return False
	return True


infile=fileinput.input()
numCases=int(infile.readline())

board = [[0 for x in range(4)] for x in range(4)] 
for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")
	dimensions = infile.readline().strip().split()
	n = int(dimensions[0])
	m = int(dimensions[1])
	
	lawn = [] 
	for x in range(0,n):
		line = infile.readline().strip().split()
		lawn.append(line)
	
	if isLawnPossible(lawn,n,m):
		print("YES")
	else:
		print("NO")
