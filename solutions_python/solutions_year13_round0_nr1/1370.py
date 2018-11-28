import sys

def run(inputFile, outputFile):
	sys.stderr.write("reading: %s, writing: %s\n" % (inputFile, outputFile))
	fin = open(inputFile)
	fout = open(outputFile, "w")
	line = fin.readline()
	n = int(line)
	for casenum in range(1, n+1):
		sys.stderr.write("doing case %d\n" %(casenum))
		line1 = [c for c in list(fin.readline().strip())]
		line2 = [c for c in list(fin.readline().strip())]
		line3 = [c for c in list(fin.readline().strip())]
		line4 = [c for c in list(fin.readline().strip())]
		fin.readline()

		result = process_case( line1, line2, line3, line4)
		msg = ""
		if result == 'X':
			msg = "X won"
		elif result == 'O':
			msg = "O won"
		elif result == '.':
			msg = "Game has not completed"
		elif result == 'c':
			msg = "Draw"
		fout.write("Case #%d: %s\n" % ( casenum, msg))
	fin.close()
	fout.close()

def process_case(line1, line2, line3, line4):
	rows = [line1, line2, line3, line4]
	for curr in rows:
		test = testwin(curr)
		if test != '.':
			return(test)
	for i in range(4):
		curr = [c[i] for c in rows]
		test = testwin(curr)
		if test != '.':
			return(test)
	d1 = [rows[0][0], rows[1][1], rows[2][2], rows[3][3]]
	test = testwin(d1)
	if test != '.':
		return(test)
	d2 = [rows[0][3], rows[1][2], rows[2][1], rows[3][0]]
	test = testwin(d2)
	if test != '.':
		return(test)

	all = set(rows[0])
	all = all.union(set(rows[1]))
	all = all.union(set(rows[2]))
	all = all.union(set(rows[3]))
	if '.' in all:
		return "."
	else:
		return "c"

def testwin(curr):
	s = set(curr)
	if not '.' in s:
		if len(s) == 1:
			if 'X' in s :
				return('X')
			if 'O' in s:
				return('O')
		if len(s)==2 and ('T' in s):
			if 'X' in s :
				return('X')
			if 'O' in s:
				return('O')
	return '.'

run(sys.argv[1], sys.argv[2])