import itertools

def solve(raw):
	start_point = int(raw.split(' ')[0])
	end_point = int(raw.split(' ')[1])

	pairs = []

	for x in range(start_point, end_point+1):
		if (x > 9):
			x = str(x)
			x_ls = []
			for i in range(len(x)):
				x_ls.append(x)
				x = x[1:] + x[0]
			for i in itertools.product(x_ls, x_ls):
				if int(i[0]) >= start_point and int(i[0]) <= end_point and int(i[1]) >= start_point and int(i[1]) <= end_point and i[0] != i[1]:
					if (i[0], i[1]) not in pairs and (i[1], i[0]) not in pairs:
						pairs.append((i[0], i[1]))


	return len(pairs)


for x in range(input()):
	print "Case #" + str(x+1) + ": " + str(solve(raw_input()))