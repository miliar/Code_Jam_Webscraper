import sys



def best_option(C, F, X, R, A):
	best = 10000000000000000000
	current = 0
	while R < 4*X:

		wait_it_out = (X - A) / R
		if wait_it_out + current < best:
			best = wait_it_out + current

		current += (C-A) / R
		R += F
	
	if current + (X - A) / R < best:
		return current + (X - A) / R
	return best

inp = open(sys.argv[1])

count = int(inp.readline())

for i in range(0, count):
	data = inp.readline().rstrip().split(" ")
	print("Case #" + str(i+1) + ": " + str(best_option(float(data[0]), float(data[1]), float(data[2]), 2.0, 0.0)))
