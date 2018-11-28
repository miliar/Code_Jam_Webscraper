infile = open('A-large.in', 'r')

n = int(infile.readline().strip())

for i in xrange(n):
	invite = 0
	cnt = 0

	j, inStr = infile.readline().strip().split()
	for k in xrange(int(j)+1):
		if cnt + invite < k:
			invite += 1
		cnt += int(inStr[k])

	print 'Case #%d: %d' % (i+1, invite)

infile.close()
