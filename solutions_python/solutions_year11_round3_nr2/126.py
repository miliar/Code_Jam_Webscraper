import sys

def space(l, t, n, c, d):
	sp0 = 0
	sp1 = 0
	i = 0
	if l==0:
		return 2*sum(d)
	while i<n and 2*sp0<t:
		sp0 += d[i]
		i += 1
	#print i, sp0, t
	if i>=n and 2*sp0<=t:
		#print '+'
		return 2*sum(d)
	if i>=n and 2*sp0>t:
		#print '-'
		return t+2*(sum(d)-t/2)
	
	sp1 = sum(d[:i])-t/2
	d1 = d[i:]
	d1.sort()
	d1.reverse()
	if len(d1)<l-1:
		sp1 += sum(d1)
	elif l-1>0:
		sp1 += sum(d1[:l-1])
		sp0 = t/2 + sum(d1[l-1:])
	else:
		sp0 = t/2 + sum(d1)
	#print sp0, sp1
	r0 = 2*sp0+sp1

	sp1 = 0
	if len(d1)<l:
		sp1 += sum(d1)
	elif l>0:
		sp1 += sum(d1[:l])
		sp0 = sum(d[:i]) + sum(d1[l:])
	else:
		sp0 = sum(d[:i]) + sum(d1)
	r1 = 2*sp0+sp1
	#print sp0, sp1
	#print r0, r1
	return min(r0, r1)

if __name__ == '__main__':
	tc = int(sys.stdin.readline())
	i = 1
	while i <= tc:
		line = [int(x) for x in sys.stdin.readline().split()]
		l = line[0]
		t = line[1]
		n = line[2]
		c = line[3]
		d0 = line[4:]
		d = []
		while len(d)<n:
			d.extend(d0)
		d = d[:n]
		print 'Case #%d:' % (i), 
		print space(l, t, n, c, d)
		i += 1
