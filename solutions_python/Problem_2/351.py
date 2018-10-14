import sys


def fread():
	try:
		inp = open(sys.argv[1], 'rt')
	except IOError:
		print 'Invalid input filename'

	out = open(sys.argv[2], 'wt')
	
	ncases = int(inp.readline())

	for i in xrange(ncases):
		t_time = int(inp.readline())
		na, nb = map(int, inp.readline().split())
		ab = []
		ba = []
		for j in xrange(na):
			ab.append(inp.readline().split())
		for j in xrange(nb):
			ba.append(inp.readline().split())

		tr = findtrains(ab, ba, t_time)
		out.write('Case #%d: %d %d\n' % (i + 1, tr[0], tr[1]))

	inp.close()
	out.close()


def findtrains(ab, ba, t_time):  # returns (tr_a, tr_b)
	adepts = []
	bdepts = []
	aarriv = []
	barriv = []

	for el in ab:
		adepts.append(el[0])
		barriv.append(el[1])

	for el in ba:
		bdepts.append(el[0])
		aarriv.append(el[1])

	tr_a = len(ab) - minustrains(adepts, aarriv, t_time)
	tr_b = len(ba) - minustrains(bdepts, barriv, t_time)

	return (tr_a, tr_b)


def minustrains(depts, arriv, t_time):
	depts.sort()
	arriv.sort()
	trains = 0

	for el in depts:
		if not arriv:
			break
		if getminutes(arriv[0]) + t_time <= getminutes(el):
			trains += 1
			arriv = arriv[1:]

	return trains


def getminutes(t):
	h, m = map(int, t.split(':'))
	return h * 60 + m


if __name__ == '__main__':
	fread()
