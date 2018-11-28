
f = open('/Users/Wanli/Downloads/D-large.in.txt')
# f = open('input.txt')
ncases = int(f.readline())

for case in range(ncases):
	num = int(f.readline())
	naomi = sorted([float(x) for x in f.readline().split()])
	ken = sorted([float(x) for x in f.readline().split()])
	naomi2 = naomi[:]
	ken2 = ken[:]

	dcount = 0
	for k in ken:
		for n in naomi2:
			if n > k:
				dcount += 1
				naomi2.remove(n)
				break

	ocount = num
	for n in naomi:
		for k in ken2:
			if k > n:
				ocount -= 1
				ken2.remove(k)
				break

	print 'Case #%d: %d %d' % (case+1, dcount, ocount)
