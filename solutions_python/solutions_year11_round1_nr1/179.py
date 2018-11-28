if __name__ == '__main__':
	fin = open("A-large.in", 'r')
	fout = open("out.txt", 'w')
	numCases = int(fin.readline())
	for item in range(numCases):
		result = "Broken"
		line = fin.readline()
		if line[-1] == '\n':
			line = line[:-1]
		line = line.split()
		N = int(line[0])
		PD = int(line[1]) * 1.0
		PG = int(line[2]) * 1.0
		if PD < 100 and PG == 100:
			fout.write('Case #%d: %s\n'%(item+1, result))
			continue
		if PD > 0 and PG == 0:
			fout.write('Case #%d: %s\n'%(item+1, result))
			continue
		if N < 100:
			for i in range(1, N+1):
				j = 0
				while j <= i:
					percent = PD * i
					if percent == j * 100:
						result = "Possible"
						break
					j += 1
				if result == "Possible":
					break
		else:
			result = "Possible"

			
		fout.write('Case #%d: %s\n'%(item+1, result))

