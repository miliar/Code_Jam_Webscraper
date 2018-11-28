import sys

#Brandon Shar
#Opera.py
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
	line = line.split()
	num_groups = int(line[0]) + 1
	groups = list(line[1])
	#current number of clapping people
	people = 0
	invites = 0
	#N
	for i in range(num_groups):
		if(people < i):
			invites += (i - people)
			people += (i - people)

		people += int(groups[i])

	#output
	output.write("Case #" + str(k+1) + ": " + str(invites) + "\n")
	




