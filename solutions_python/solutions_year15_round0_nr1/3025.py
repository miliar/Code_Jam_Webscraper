filename = "A-large.in"
f = open(filename, 'r')
testcases = int(f.readline())
for i in range(testcases):
	line = f.readline().split()
	max_shy = int(line[0])
	audience = list(int(d) for d in line[1])
	output = 0
	current_standing = 0
	for j in range(max_shy + 1):

		if audience[j] > 0:
			if j <= current_standing:

				current_standing += audience[j]
			else:
				output += j - current_standing
				current_standing = j + audience[j]

	print "Case #" + str(i+1) + ": " + str(output)