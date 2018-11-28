def chkConvert(status, row, col, i, j):
	if i + 1 > row:
		return False
	if j + 1 > col:
		return False
	if not (status[i+1][j] == "#"):
		return False
	if not (status[i][j+1] == "#"):
		return False
	if not (status[i+1][j+1] == "#"):
		return False
	status[i][j] = '/'
	status[i][j+1] = '\\'
	status[i+1][j] = '\\'
	status[i+1][j+1] = '/'
	return True

if __name__ == '__main__':
	fin = open("A-large.in", 'r')
	fout = open("alarge.txt", 'w')
	numCases = int(fin.readline())
	for item in range(numCases):
		line = fin.readline()
		if line[-1] == '\n':
			line = line[:-1]
		line = line.split()
		row = int(line[0])
		col = int(line[1])
		status = []
		for i in range(row):
			line = fin.readline()
			if line[-1] == '\n':
				line = line[:-1]
			ln = []
			for j in range(col):
				ln.append(line[j])
			status.append(ln)
		result = ""
		for i in range(row):
			for j in range(col):
				if status[i][j] == '#':
					if not chkConvert(status, row - 1, col - 1, i, j):
						result = "impossible"
						break
			if result == "impossible":
				break
		if not (result == "impossible"):
			result = status
		else:
			result = ["Impossible"]
		fout.write('Case #%d:\n'%(item+1))
		for data in result:
			fout.write('%s\n'%(''.join(data)))
fout.close()
fin.close()


