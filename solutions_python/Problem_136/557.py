
ff = open('/Users/Wanli/Downloads/B-large.in.txt')
# ff = open('input.txt')
ncases = int(ff.readline())

for case in range(ncases):
	tokens = ff.readline().split()
	c = float(tokens[0])
	f = float(tokens[1])
	x = float(tokens[2])

	nfarms = 0
	total = 0
	time1 = x / 2
	time2 = c / 2 + x / (2 + f)
	while time1 > time2:
		total += c / (2 + f * nfarms)
		nfarms += 1
		time1 = x / (2 + f * nfarms)
		time2 = c / (2 + f * nfarms) + x / (2 + f * (nfarms + 1))
	total += time1

	print 'Case #%d: %f' % (case+1, total)
