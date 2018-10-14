'''
Standing Ovation
'''

if __name__ == '__main__':
	f=open("A-large.in")
	s = ""
	nc=int(f.readline())
	for x in xrange(1,nc+1):
		(smax, shyness) = f.readline().strip('\n').split(' ')
		a = 0
		nf = 0
		for k,p in enumerate(shyness):
			if k > smax:
				break
			if not int(p):
				continue 
			if a >= k:
				a += int(p)
			else:
				nf += k - a
				a = k + int(p)
		print "Case #%d: %d" % (x, nf)