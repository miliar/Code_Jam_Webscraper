# Open files
inf = open('B-large.in', 'r')
outf = open('out.txt', 'w')

# Read in number of test cases
n = int(inf.readline().strip())

#Loop through test cases
for i in xrange(n):
	ans = 0.0

	data = inf.readline().strip().split()
	c = float(data[0])
	f = float(data[1])
	x = float(data[2])

	rate = 2.0


	while True:
		if x / rate <= c/rate + x/(rate+f):
			ans += x/rate
			break
		else:
			ans += c/rate
			rate += f

	#print 'Case #%d: %.7f\n' % (i, ans)
	outf.write('Case #%d: %.7f\n' % (i+1, ans))

# Close input and output files
inf.close()
outf.close()