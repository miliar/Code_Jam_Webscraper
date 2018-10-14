def _getRecycled(n):
	res = map( lambda x: n[x:] + n[:x], range(0,len(n)) )
	return filter( lambda x: x[0] != '0' and n < x, res)


if __name__ == "__main__":
	T = int(raw_input())

	for c in xrange(1,T+1):
		A, B = raw_input().split(' ')

		if int(B) < 10:
			print "Case #%s: 0" % c
			continue
		
		res = 0
		_all = []

		for i in xrange(int(A), int(B)):
			rec = _getRecycled(str(i))

			if rec != None: 
				rec = filter(lambda x: x <= B, rec)
				for t in map(lambda x: (str(i), str(x)), rec): _all.append(t)

		if _all != None:
			for i in _all:
				if(_all.count(i) > 1): _all.remove(i)
			res += len(_all)


		print "Case #%s: %s" % (c, res)