def xsum(l):
	x = l[0]
	for i in range(1, len(l)):
		x ^= l[i]
	return x

f = open('C-large.in', 'r')

T = int(f.readline()[:-1])
for case_no in range(1, T + 1):
	N = int(f.readline()[:-1])
	L = map(int, f.readline()[:-1].split(' '))

	patrick = xsum(L)
	if patrick:
		print "Case #%s: %s" % (case_no, 'NO')
	else:
		L.sort()
		for candy in L:
			sean = L
			sean.remove(candy)
			if candy ^ xsum(sean) == 0:
				print "Case #%s: %s" % (case_no, sum(sean))

