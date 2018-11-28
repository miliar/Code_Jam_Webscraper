'''
Deceitful War
'''
if __name__ == '__main__':
	f=open("D-large.in")
	s = ""
	nc=int(f.readline())
	for x in xrange(1,nc+1):
		nb=int(f.readline())
		n=map(float, f.readline().strip('\n').split(" "))
		k=map(float, f.readline().strip('\n').split(" "))
		n.sort()
		k.sort()
		nt = [1]*nb
		kt = [1]*nb
		w = w1 = 0
		for i in xrange(nb):
			for j in xrange(nb):
				if n[i] < k[j] and nt[i] == 1 and kt[j] == 1:
					nt[i] = 0
					kt[j] = 0
					w += 1
		nt = [1]*nb
		kt = [1]*nb
		for i in xrange(nb):
			for j in xrange(nb):
				if n[i] > k[j] and nt[i] == 1 and kt[j] == 1:
					nt[i] = 0
					kt[j] = 0
					w1 += 1
					break

		print "Case #%d: %d %d" % (x, w1, nb-w)