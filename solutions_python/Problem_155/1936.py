import sys

input_file = open(sys.argv[1], 'r')
for x in xrange(0, int(input_file.readline())):
	inp = input_file.readline().split()

	friends = 0
	clapping = 0
	cases = inp[1]

	for i in xrange(0, len(cases)):
		if clapping - i < 0:
			friends += i - clapping
			clapping += i - clapping
		clapping += int(cases[i])

	print("Case #{}: {}".format(x + 1, friends))