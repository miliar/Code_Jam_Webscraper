import sys

inputData = open(sys.argv[1]).read().strip().split("\n")
outputFile = open(sys.argv[2],"w")
cases = int(inputData[0])
inputData = inputData[1:]
for i in range(cases):
	outputFile.write("Case #"+str(i+1)+": ")
	A = int(inputData[i].split(" ")[0])
	B = int(inputData[i].split(" ")[1])
	x = 0
	for n in range(A,B):
		s = str(n)
		if len(s) == 1:
			break
		else:
			for i in range(len(s)-1):
				s = s[-1] + s[0:-1]
				m = int(s)
				if m <= B and m > n:
					x+=1
	outputFile.write(str(x))	
	outputFile.write("\n")
