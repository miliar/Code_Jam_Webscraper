inp = open("A-large.in", "r")
R=lambda:map(int, inp.readline().strip().split(' '))
SR=lambda:map(str, inp.readline().strip().split(' '))
oup = open("output.txt", "w")

t, = R()
print t
for i in range(t):
	oup.write('Case #%d: ' % (i + 1))

	shy, snum = SR()
	num = [int(i) for i in snum]
	shy = int(shy)
	if shy == 0:
		oup.write('0\n')
		continue

	total = num[0]
	inc = 0
	for level in xrange(1, shy+1):
		if total < level:
			inc += level - total
			total = level
		total += num[level]
	oup.write('%d\n' % (inc))
