import sys

#Brandon Shar
#ominos.py
#
#No error handling exists in this program, it must be executed with two command line params
#the first for the file path for input data, the second for output
#and all input is assumed to be valid

inFile = sys.argv[1]
outFile = sys.argv[2]


file = open(inFile)
output = open(outFile, 'w')

tests = file.readline()

#get test cases
for k in range(int(tests)):
	line = file.readline()
	line = file.readline()
	mushrooms = [int(i) for i in line.split()]

	eaten1 = 0
	eaten2 = 0
	pace = 0
	for i in range(len(mushrooms)-1):
		if(mushrooms[i+1] < mushrooms[i]):
			eaten1 = eaten1 + (mushrooms[i] - mushrooms[i+1])

		if((mushrooms[i] - mushrooms[i+1]) > pace):
			pace = (mushrooms[i] - mushrooms[i+1])

	print(pace)
	for i in range(len(mushrooms)-1):
		if(pace < mushrooms[i]):
			eaten2 += pace
		else:
			eaten2 += mushrooms[i]

	output.write("Case #" + str(k+1) + ": " + str(eaten1) + " " + str(eaten2) + "\n")



