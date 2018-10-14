def xor_sum(lst) :
	y = 0
	for x in lst :
		y = int(y) ^ int(x)
	return int(y)

f=open(r'C_smallinput.in', 'r')
t=f.readline()
t=t.rsplit( )[0]
t=int(t)
# print t
import itertools

for k in range(1, t+1) :
	n=f.readline()
	n=n.rsplit( )[0]
	n=int(n)
	# print n
	line=f.readline()
	line=line.rstrip("\n\r ")	
	lst=line.split(' ')
	m = 0
	for i in range(1, n/2+1) :
		p = itertools.combinations(lst, i)
		for r in p :
			r = list(r)
			q = []
			for i in range(0, len(lst)) :
				q.append( lst[i])
			#  q = list(set(lst).difference(r))
			for x in r:
 				q.remove(x)
			for j in range(0,len(r))  :
				r[j] = int(r[j])
			for j in range(0,len(q))  :
				q[j] = int(q[j])
			#  print r, q
			if xor_sum(r) == xor_sum(q) :
				ma = max( sum(r), sum(q))
				m = max(m, ma)
				
	if m == 0 :
		print 'Case #{0}: NO'.format(k)
	else :
		print 'Case #{0}: {1}'.format(k, m)