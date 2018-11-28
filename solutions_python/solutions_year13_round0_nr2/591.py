import sys

args = sys.argv[1:]

fname = args[0]

f = open(fname)

T = f.readline()
T = int(T)

for t in range(T):
	case_number = t + 1

	line = f.readline().strip()
	line = line.split(" ")
	N = int(line[0])
	M = int(line[1])

	lawn = []

	tallest_in_row = [] # N elements
	tallest_in_col = [0 for _ in range(M)] # M elements
	

	for n in range(N):
		line = f.readline().strip()
		line = line.split(" ")

		lawn.append([int(el) for el in line])

		this_row = lawn[-1]
		tallest_in_row.append(max(this_row))

		tallest_in_col = [max(this_row[m], tallest_in_col[m]) for m in range(M)]

	#print lawn
	#print tallest_in_row
	#print tallest_in_col

	ok = True
	for n in range(N):
		for m in range(M):
			if lawn[n][m] < tallest_in_row[n] and lawn[n][m] < tallest_in_col[m]:
				ok = False
				break
		if not ok:
			break

	if ok:
		print "Case #%d: YES" % case_number
	else:
		print "Case #%d: NO"  % case_number

