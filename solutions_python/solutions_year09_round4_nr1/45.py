def solve():
	n = int(raw_input())
	ls = []
	for i in xrange(n):
		l = raw_input()
		k = 0
		for j in xrange(n):
			if l[j] == '1':
				k = j+1
		ls.append(k)
	count = 0
	for i in xrange(1, n+1):
		icnt = 0
		for idx, j in enumerate(ls):
			if j <= i:
				ls[idx] = '#'
				break
			elif j != '#':
				icnt += 1
		count += icnt
	print count

if __name__=='__main__':
	tn = int(raw_input())
	for loop in xrange(tn):
		print 'Case #%d:' % (loop+1),
		solve()
