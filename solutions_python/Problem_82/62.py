import copy
if __name__ == '__main__':
	fin = open("B-large.in", 'r')
	fout = open("11BBLarge.txt", 'w')
	numCases = int(fin.readline())
	for item in range(numCases):
		line = fin.readline()
		if line[-1] == '\n':
			line = line[:-1]
		line = line.split()
		N = int(line[0])
		D = int(line[1])
		collec = []
		for group in range(N):
			line = fin.readline()
			if line[-1] == '\n':
				line = line[:-1]
			line = line.split()
			P = int(line[0])
			V = int(line[1])
			collec.append((P,V))
		collec.sort(key = lambda t: t[0])
		result = 0.0
		initi = 0
		for i in range(N):
			j = N - 1
			while True:
				if i > j:
					break
				p = copy.deepcopy(i)
				total = 0
				while j >= p:
					total += collec[p][1]
					p += 1
				required = (total - 1) * D
				tempResult = required - (collec[j][0] - collec[i][0])
				if tempResult > result:
					result = tempResult
				j -= 1
		fout.write('Case #%d: %s\n'%(item+1, (result*1.0)/2))


