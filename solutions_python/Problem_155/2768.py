t = int(raw_input())

for c in range(1, t + 1):
	line = raw_input().split()
	smax = int(line[0])
	seq  = line[1]

	res = 0
	count = 0
	for i in range(0, smax + 1):
		if int(seq[i]) > 0 and i > count:
			res += i - count
			count += i - count
		count += int(seq[i])

	print "Case #%d: %d" % (c, res)

