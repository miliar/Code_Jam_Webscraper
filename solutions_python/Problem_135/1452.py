def solve():
	pass


def read_ints(f):
	return [int(w) for w in f.readline().strip().split()]

def read_int(f):
	return int(f.readline().strip())


from sys import argv

f = open(argv[1])

T = read_int(f);

for t in range(1, T+1):
	c1 = read_int(f)
	g1 = [read_ints(f) for _ in range(4)]
	c2 = read_int(f)
	g2 = [read_ints(f) for _ in range(4)]

	r1 = g1[c1-1]
	r2 = g2[c2-1]

	vals = []
	for i in range(1, 17):
		if i in r1 and i in r2:
			vals.append(i)

	nv = len(vals)
	if nv == 0:
		res = 'Volunteer cheated!'
	elif nv == 1:
		res = vals[0]
	else:
		res = 'Bad magician!'

	print 'Case #%s: %s' % (t, res)
