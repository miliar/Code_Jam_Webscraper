import sys

inputData = open(sys.argv[1]).read().strip().split("\n")
outputFile = open(sys.argv[2],"w")
cases = int(inputData[0])
inputData = inputData[1:]
for i in range(cases):
	outputFile.write("Case #"+str(i+1)+": ")
	case = inputData[i].split(" ")
	n = int(case[0])
	s = int(case[1])
	p = int(case[2])
	x = 0
	case = case[3:]
	case.sort()
	for item in case:
		item = int(item)
		if p == 0:
			x += 1
			continue
		if p == 1:
			if item >= 1:
				x += 1
			continue
		if item < (3*p-4) or item < p:
			continue
		if item > (3*p+4):
			x += 1
		elif item >= 3*p-2 and item <= 3*p+2 :
			x += 1
		elif item == 3*p-4 or item == 3*p-3:
			if s > 0:
				x += 1
				s -= 1
		elif item == 3*p+3 or item == 3*p+4:
			if s > 0:
				s -= 1
			x += 1
	print p, s, x
	outputFile.write(str(x) + "\n")
