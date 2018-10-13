#f = open('C0.testPy', 'w')
#o = open('C0.table', 'w')
o2 = open('C0.table2', 'w')
MAXL = 100
sp = []
p = [0 for i in xrange(MAXL)]
p2 = [0 for i in xrange(MAXL)]
def fill(d, l):
	if d == ((l+1) >> 1):
		pn = 0
		base = 1
		for i in range(d):
			pn += p[i] * base
			base *= 10
		for i in range(d):
			ri = d-1-i;
			if (l-1-ri == ri):
				continue
			pn += p[ri] * base
			base *= 10
		pn2 = pn * pn
		#f.write('l=%d P=%d P2=%d\n'%(l, pn, pn2))
		l2 = 0
		pn2_ = pn2
		while pn2_ > 0:
			p2[l2] = pn2_ % 10
			pn2_ /= 10
			l2 += 1
		ok = True
		for i in range(l2 >> 1):
			ok = (p2[i] == p2[l2-1-i])
			if not ok:
				break
		if ok:
			sp.append(pn2)
			#f.write('OK!\n')
			#o.write('%d\n'%pn2)
			o2.write('%s\n'%str((pn, pn2)))
	else:
		if d > 0:
			p[d] = 0
			fill(d+1, l)
		p[d] = 1
		fill(d+1, l)
		if d == 0 or d == ((l+1) >> 1)-1:
			p[d] = 2
			fill(d+1, l)
if __name__ == '__main__':
	for l in range(1, ((MAXL+1) >> 1)+1):
		print 'L=', l
		fill(0, l)
		print sp
		sp = []
#	print sp

