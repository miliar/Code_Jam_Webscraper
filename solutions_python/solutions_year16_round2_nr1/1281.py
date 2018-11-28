import math

def readandwritefile(filein, fileout):
	with open(filein) as f:
		lines = f.readlines()
		curline = 0
		numcases = int(lines[curline].rstrip())
		curline += 1
		linestowrite = []
		for i in range(1, (numcases+1)):
			linestowrite.append(solve(lines[curline].rstrip().split()))
			curline += 1
		writeanswer(linestowrite, fileout)
		f.close()

def writeanswer(lines, file):
	with open(file, 'w+') as f:
		for i in range(0 ,len(lines)):
			line = lines[i]
			f.write("Case #" + str(i+1) + ": " + line)
			if(i+1 < len(lines)):
				f.write("\n")
		f.close()






def solve(params):
	entry = ""
	block = params[0]
	checkmark = {}
	for i in range(0, len(block)):
		if block[i] in checkmark:
			checkmark[block[i]] += 1
		else:
			checkmark[block[i]] = 1
	nums = []
	oscounted = 0
	sscounted = 0
	nscounted = 0
	vscounted = 0
	hscounted = 0
	if "Z" in checkmark:
		for i in range(0, checkmark["Z"]):
			nums.append(0)
		oscounted += checkmark["Z"]

	if "W" in checkmark:
		for i in range(0, checkmark["W"]):
			nums.append(2)
		oscounted += checkmark["W"]

	if "U" in checkmark:
		for i in range(0, checkmark["U"]):
			nums.append(4)
		oscounted += checkmark["U"]

	if "X" in checkmark:
		for i in range(0, checkmark["X"]):
			nums.append(6)
		sscounted += (checkmark["X"])

	if "G" in checkmark:
		for i in range(0, checkmark["G"]):
			nums.append(8)
		hscounted += checkmark["G"]

	if "S" in checkmark:
		for i in range(0, checkmark["S"] - sscounted):
			nums.append(7)
		vscounted += (checkmark["S"] - sscounted)
		nscounted += (checkmark["S"] - sscounted)

	if "O" in checkmark:
		for i in range(0, checkmark["O"] - oscounted):
			nums.append(1)
		nscounted += (checkmark["O"] - oscounted)

	if "V" in checkmark:
		for i in range(0, checkmark["V"] - vscounted):
			nums.append(5)
		sscounted += checkmark["V"] - vscounted

	if "N" in checkmark:
		for i in range(0, (checkmark["N"] - nscounted)/2):
			nums.append(9)

	if "H" in checkmark:
		for i in range(0, checkmark["H"] - hscounted):
			nums.append(3)

	nums.sort()
	for i in range(0, len(nums)):
		entry += str(nums[i])
	return entry




readandwritefile('file.in', 'file.out')