def lawncheck(w,h,vlist,hlist):
	for x in xrange(w):
		for y in xrange(h):
			cval = vlist[x][y]
			vmax = max(vlist[x])
			hmax = max(hlist[y])
			if cval not in (vmax,hmax):
				return "NO"
	return "YES"

if __name__ == "__main__":
	for tcase in xrange(1,int(raw_input())+1):
		h,w = [int(c) for c in raw_input().split()]
		hlist = []
		vlist = [list() for i in xrange(w)]
		for y in xrange(h):
			nl = [int(n) for n in raw_input().split()]
			hlist.append(nl)
			for l,n in zip(vlist,nl):
				l.append(n)
		print "Case #%d: %s" % (tcase,lawncheck(w,h,vlist,hlist))
