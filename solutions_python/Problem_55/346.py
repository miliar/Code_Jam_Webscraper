def roller(r, k, l, n):
	seq = {}
	p = 0
	while r > 0:
		tl = tuple(l)
		if tl in seq:
			d = seq[tl][2]-r
			tp = p-seq[tl][3] #How many did we earn since we saw this list?
			q = r/d
			if q>=1: #If we can repeat the operation, all good.
				p += tp*q
				r = r%d
				continue
			else:
				l = seq[tl][1]
				p += seq[tl][0]
			
		else:
			t = k
			i = n
			while (t-l[0])>=0 and i>0:
				t-=l[0]
				l.append(l.pop(0))
				i -= 1
			tp = k-t
			seq[tl] = (tp, l[:], r, p)
			p += tp
		r -= 1
	return p

if __name__ == '__main__':
	N = int(raw_input())
	for i in range(1, N+1):
		r, k, n = (int(j) for j in raw_input().split())
		l = [int(j) for j in raw_input().split()]
		print "Case #%d: %s" % (i, roller(r, k, l, n))
