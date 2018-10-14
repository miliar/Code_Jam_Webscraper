def get_recycled (n, B):
	rec = []
	sn = str(n)

	for i in xrange(0, len(sn)):
		sm = sn[i:] + sn[:i]
		m = int(sm)

		# make sure length is still the same (eg don't want leading zeroes, etc)
		if len(str(m)) != len(sn):
			continue

		if n < m and m <= B:
			if m not in rec:
				rec.append (m)

	return len(rec)


if __name__ == "__main__":
	with open('C-large.in') as f:
		f.next() 	# skip first line
		case = 1
		for line in f:
			As, Bs = line.strip().split()
			A = int(As)
			B = int(Bs)

			total_recycled = 0

			for n in xrange (A, B):
				total_recycled += get_recycled (n, B)

			print 'Case #%d: %d' % (case, total_recycled)
			case += 1