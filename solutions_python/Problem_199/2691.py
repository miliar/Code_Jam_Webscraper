import sys
import time

inputfile = open(sys.argv[1],'r')
outputfile = open(sys.argv[1].replace("in","out"),'w')

testcases = int(inputfile.readline())

for i in range(0, testcases):
	stack_line = inputfile.readline()
	stack = stack_line.split(" ")[0]
	num_pancake = int(stack_line.split(" ")[1])
	print str(stack) +": " + str(num_pancake)

	flips = 0

	if "-" not in stack:
		flips = 0

	while "-" in stack:
		index = stack.find("-")
		if index + num_pancake > len(stack):
			flips = -1
			outputfile.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")
			break
		stack = stack[:index] + stack[index:index+num_pancake].replace('-','|').replace('+','-').replace('|','+') + stack[index+num_pancake:]
		print stack
		flips = flips + 1
		
	if flips >= 0:
		outputfile.write("Case #" + str(i+1) + ": " + str(flips) + "\n")
outputfile.close()
