import re
from collections import deque

def solution(A, B):
	numPairs = 0
	nperms = len(str(A)) - 1
	for i in xrange(A, B):
		d = deque(str(i))
		qpairs = []
		for j in range(nperms):
			d.rotate(1)
			if d[0] == '0':
				continue
			p2 = int("".join(d))
			if (p2 <= i or p2 > B or (p2 in qpairs)):
				continue
			qpairs.append(p2)
			numPairs += 1
	return numPairs

def readAndProcessInput(file_name, output_file_name=None):
	input_file = open(file_name, "r")
	if not output_file_name:
		output_file = open(file_name[0:-2]+"out", "w")
	else:
		output_file = open(output_file_name, "w")
	sNumCases = re.search(r"[\d]+", input_file.readline())
	if sNumCases:
		num_cases = int(sNumCases.group())
		for i in range(num_cases):
			l = input_file.readline()
			if l:
				A = 0
				B = 0
				position = 0
				for m in re.finditer(r"[\d]+",l):
					if position==0:
						A = int(m.group())
					elif position == 1:
						B = int(m.group())
					position += 1
				sol = solution(A, B)
				pl = "Case #x: y".replace("x", str(i+1)).replace("y", str(sol)) + "\n"
				output_file.write(pl)
	input_file.close()
	output_file.close()