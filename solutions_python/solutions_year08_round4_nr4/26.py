# coding: utf8
import sys

if len(sys.argv) > 1:
	f_name = sys.argv[1]
else:
	f_name = "B.in"

fh = open(f_name)
N = int(fh.readline())


def perm_gn(k):
	if k == 1:
		yield (0,)
	else:
		for perm in perm_gn(k-1):
			for i in xrange(k):
				p = list(perm)
				p.insert(i, k-1)
				yield tuple(p)
		
def perm_size(S, p, k):
	count	= 0
	c_l	= None
	for i in xrange(len(S)):
		ik = i % k
		c = S[i - ik + p[ik]]
		if c != c_l:
			count += 1
			c_l = c
	return count
	

for i in xrange(N):
	k = int(fh.readline())
	S = fh.readline().strip()

	min_l = len(S)
	for p in perm_gn(k):
		min_l = min(perm_size(S, p, k), min_l)
		

	print "Case #%d: %s" % (i+1, min_l)


