import sys

def fun(q):
	e = [int(d) for d in str(q)]
	r = sorted(e)
	if e != r:
		if q % 100 == 10:
			l = len(str(q))
			num = 1
			for a in range(1, l-1):
				num += 10 ** a
			q = q - num
			return fun(q)
		else:
			w = q % 10
			w += 1
			q -= w
			return fun(q)
	# else:
	# 	continue
	return q

f = open('out.txt', 'w')
with open(sys.argv[1], 'r') as fd:
	T = int(fd.readline())
	N = [fd.readline().strip().split(' ') for i in range(T)]
	e = []
	for n,z in zip(N,range(1, T+1)):
		q = int(n[0])
		# e = [int(d) for d in str(q)]
		# r = sorted(e)
		stn = fun(q)
		print >> f, "Case #%d:"%z, stn
f.close()