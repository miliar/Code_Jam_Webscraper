import sys

inputpath = sys.argv[1]
outputpath = sys.argv[2]

infile = open(inputpath, "r")
outfile = open(outputpath, "w")
T = int(infile.readline())
for test in range(T):
	N = int(infile.readline())
	m = list(map(int, infile.readline().split()))
	first = 0
	second = 0
	max_difference = 0
	for k in range(1,len(m)):
		if m[k] < m[k-1]:
			first += m[k-1]-m[k]
		if m[k-1] - m[k] > max_difference:
			max_difference = m[k-1] - m[k]
	for k in m[:-1]:
		second += min(k, max_difference)
	outfile.write("Case #{}: {} {}\n".format(test+1, first, second))
outfile.close()
infile.close()
