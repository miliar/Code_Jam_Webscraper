#! /usr/bin/python

import sys

def perms(xs,ys,cache):
	if (xs,ys) in cache: return cache[(xs,ys)]
	nxs,nys = len(xs),len(ys)
	if nxs == 0:
		ret = 1
	elif nys == 0:
		ret = 0
	elif nxs == 1 and nys == 1:
		if xs[0] == ys[0]:	ret = 1
		else:			ret = 0
	elif xs[0] == ys[0]:
		ret = perms(xs,ys[1:],cache) + perms(xs[1:],ys[1:],cache)
	else:
		ret = perms(xs,ys[1:],cache)
	cache[(xs,ys)] = ret
	return ret

if __name__ == '__main__':

	tests = int(sys.stdin.readline().strip())
	gcg = 'welcome to code jam'
	
	for i in xrange(1,tests+1):
		l = sys.stdin.readline().strip()
		n = perms(gcg,l,  dict() )
		print "Case #%d: %s" % (i, str(n)[-4:].zfill(4))
