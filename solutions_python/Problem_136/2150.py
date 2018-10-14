fin = open('./B-large.in', 'r')
fout = open('./cookielarge.out', 'w')
numCases = int(fin.readline())
for i in range(numCases):
	data = fin.readline().split()
	c = float(data[0])
	f = float(data[1])
	x = float(data[2])
	a = 1
	prev = x/2
	currc = c/2
	while currc + x/(a*f+2) < prev:
		rate = a*f+2
		prev = currc + x/rate
		currc += c/rate
		a += 1
	print >> fout, "Case #%d: " % (i+1) + "%.7f" % prev
			

