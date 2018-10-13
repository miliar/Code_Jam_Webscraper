if __name__ == '__main__':
	fin = open("C-small-attempt0.in", 'r')
	fout = open("csmall.txt", 'w')
	numCases = int(fin.readline())
	for item in range(numCases):
		line = fin.readline()
		if line[-1] == '\n':
			line = line[:-1]
		line = line.split()
		N = int(line[0])
		lowest = int(line[1])
		highest = int(line[2])

		line = fin.readline()
		if line[-1] == '\n':
			line = line[:-1]
		line = line.split()
		oth = []
		for data in line:
			oth.append(int(data))
		result = 0
		maxscore = 0
		freq = lowest
		while freq <= highest:
			score = 0
			for data in oth:
				if not(data % freq):
					score +=1
				elif not(freq % data):
					score +=1
				else:
					score = 0
					break
			if score > maxscore:
				maxscore = score
				result = freq
			freq += 1
		if result == 0:
			result = "NO"
		fout.write('Case #%d: %s\n'%(item+1, result))
fout.close()
fin.close()


