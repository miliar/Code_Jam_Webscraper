# Test cases
t = 0

# Input file
ip = open("A-small-attempt0.in", 'r')
# Output file
op = open("output.txt", 'w')

# Reading test cases
t = int(ip.readline().rstrip())
for i in range(t):
	# Row number 1
	row1 = 0
	# Arrangement 1
	arr1 = []
	# Row number 2
	row2 = 0
	# Arrangement 2
	arr2 = []
	# Counter
	c = 0
	# Output
	y = 0
	# Row number
	row1 = int(ip.readline().rstrip())
	print row1 ####
	for j in range(4):
		arr1.append(ip.readline().rstrip().split(' '))
	print arr1	####
	row2 = int(ip.readline().rstrip())
	print row2	####
	for j in range(4):
		arr2.append(ip.readline().rstrip().split(' '))
	print arr2	####
	for k in arr1[row1 - 1]:
		print k	####
		if k in arr2[row2 - 1]:
			y = k
			c += 1
		print c 	####

	if c == 1:
		op.write("Case #" + str(i+1) + ": " + y +'\n')
	elif c > 1:
		op.write("Case #" + str(i+1) + ": " + "Bad magician!"+'\n')
	else:
		op.write("Case #" + str(i+1) + ": " + "Volunteer cheated!"+'\n')


