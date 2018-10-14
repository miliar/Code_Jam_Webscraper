def calc_case(N, S, p, sums):
	n = 0
	m = 0
	for s in sums:
		if s >= 3 * p - 2:
			n += 1
		elif s >= 3 * p - 4 and p >= 2:
			m += 1

	z = n + min(m, S) 

	return z

def write_case(i, z, o):
	o.write('Case #' + str(i) + ': ' + str(z) + '\n')

f = open('b_in_large.txt')
o = open('b_large.txt', 'w')
Count = int(f.readline())

i = 1
for l in f:
	x = [int(x) for x in l.split()]
	z = calc_case(x[0], x[1], x[2], x[3:])
	write_case(i, z, o)
	i += 1

o.close()
f.close()