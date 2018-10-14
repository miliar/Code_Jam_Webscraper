import sys

def run(inputFile, outputFile):
	sys.stderr.write("reading: %s, writing: %s\n" % (inputFile, outputFile))
	fin = open(inputFile)
	fout = open(outputFile, "w")
	line = fin.readline()
	n = int(line)
	for casenum in range(1, n+1):
		sys.stderr.write("doing case %d\n" %(casenum))
		line = fin.readline().split(" ")
		n = int(line[0])
		m = int(line[1])
		lawn = []
		for i in range(n):
			lawn.append([int(c) for c in fin.readline().split()])

		result = process_case( n, m, lawn )
		str = "NO"
		if result:
			str = "YES"
		fout.write("Case #%d: %s\n" % ( casenum, str))
	fin.close()
	fout.close()

def process_case(n, m, lawn):
	colmaxs = []
	colmins = []
	rowmaxs = []
	rowmins = []
	for i in range(n):
		minval = 100
		maxval = 1
		for j in range(m):
			if lawn[i][j] < minval:
				minval = lawn[i][j]
			if lawn[i][j] > maxval:
				maxval = lawn[i][j]
		rowmins.append(minval)
		rowmaxs.append(maxval)
	for j in range(m):
		minval = 100
		maxval = 1
		for i in range(n):
			if lawn[i][j] < minval:
				minval = lawn[i][j]
			if lawn[i][j] > maxval:
				maxval = lawn[i][j]
		colmins.append(minval)
		colmaxs.append(maxval)

	for i in range(n):
		for j in range(m):
			if lawn[i][j] > rowmins[i]:
				for k in range(m):
					if lawn[i][k] < lawn[i][j] and colmaxs[k] > lawn[i][k]:
						return(0)
			if lawn[i][j] > colmins[j]:
				for k in range(n):
					if lawn[k][j] < lawn[i][j] and rowmaxs[k] > lawn[k][j]:
						return(0)

	return(1)

run(sys.argv[1], sys.argv[2])