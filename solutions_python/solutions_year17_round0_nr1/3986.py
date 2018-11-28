import sys
from collections import deque

def getMinFlipCount(pancakes,panSize):
	pancakes = convertCakesToBoolean(pancakes)
	if not any(pancakes):
		return 0
	observed = set()
	q = deque()
	q.append((pancakes,0))
	while q:
		cakes,flips = q.pop()
		observed.add(tuple(cakes))
		for i in range(0,len(cakes)-panSize+1):
			tmpCakes = list(cakes)
			for j in range(i,i+panSize):
				tmpCakes[j] = not tmpCakes[j]
			if tuple(tmpCakes) in observed:
				continue
			if any(tmpCakes):
				q.appendleft((tmpCakes,flips+1))
			else:
				return flips+1
	return 'IMPOSSIBLE'

def convertCakesToBoolean(pancakes):
	return [True if x == '-' else False for x in pancakes]

def main(inputFile,outFile):
	with open(inputFile,'r') as fin, open(outFile,'w') as fout:
		T = fin.readline()
		for i,line in enumerate(fin):
			S,K = line.strip().split()
			fout.write('Case #{0}: {1}\n'.format(i+1,getMinFlipCount(S,int(K))))

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])
