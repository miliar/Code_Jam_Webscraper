tests = int(raw_input())

for i in range(tests):
	print 'Case #%d:' % (i + 1), 
	n = raw_input()
	l = len(n)
	if l == 1:
		print n
		continue
	if '1' * l > n:
		print '9' * (l - 1)
		continue
	result = ''
	for i in range(l):
		d = '0'
		for dig in range(10):
			cur = result + str(dig) * (l - i)
			if cur <= n:
				d = str(dig)
		result += d
	print result