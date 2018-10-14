import sys

special = [1,4,9,121,484]
infile = open(sys.argv[1])
num = int(infile.readline())
for i in range(num):
	counter = 0
	current = list(infile.readline().split())
	for j in range(int(current[0]), int(current[1])+1):
		if j in special:
			counter += 1
	index = str(i+1)
	print "Case #" + index + ": " + str(counter)