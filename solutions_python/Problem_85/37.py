if __name__ == '__main__':
	fin = open("B-large (1).in", 'r')
	fout = open("blarge.txt", 'w')
	numCases = int(fin.readline())
	for item in range(numCases):
		line = fin.readline()
		if line[-1] == '\n':
			line = line[:-1]
		line = line.split()
		L = int(line[0])
		t = int(line[1])
		N = int(line[2])
		C = int(line[3])
		data = line[4:]

		initi = t/2
		absdata = []
		j = 0
		dist = 0
		tempRes = 0
		startApp = False
		i = 0
		while True:
			if j >= N:
				break
			if i == C:
				i = 0
			if startApp:
				absdata.append(int(data[i]))
			elif (dist + int(data[i])) > initi:
				absdata.append(dist + int(data[i]) - initi)
				startApp = True
			else:
				tempRes += 2 * int(data[i])
				dist += int(data[i])

			i += 1
			j += 1
		if startApp:
			absdata.sort(cmp = lambda x, y: cmp(y, x))
			result = t
			for i in absdata:
				if L:
					L -= 1
					result += i
				else:
					result += i*2
		else:
			result = tempRes
		
		
		fout.write('Case #%d: %s\n'%(item+1, result))
fout.close()
fin.close()


