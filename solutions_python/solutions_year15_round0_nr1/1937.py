
def process(tokens):
	num_friends = 0
	tot = 0
	for i,c in enumerate(tokens[1]):
		if tot < i:
			num_friends += i - tot
			tot = i
		tot += int(c)
	return num_friends


f = open('b1.txt', 'r')
tmp = f.readline()
i = 0
for line in f:
	i += 1
	tokens = line.rstrip().split()
	output = process(tokens)
	print "Case #%d: %d" % (i, output)
		
