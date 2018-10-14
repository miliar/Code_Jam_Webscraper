def solve(ps, k):
	row = [v == '+' for v in ps]
	n = 0

	def flip(row, k, p):
		# print "flip(%s, %d, %d)" % (['+' if v else '-' for v in row], k, p)
		return [
			not v if i >= p and i < k+p else v
			for i, v in enumerate(row)
		]

	if not row[-1]:
		n += 1
		row = flip(row, k, len(row)-k)
		# print row
	
	for i in range(0, len(row)-k):
		if not row[i]:
			n += 1
			row = flip(row, k, i)
			# print row
	if set(row) == {True}:
		return n
	return "IMPOSSIBLE"

for ln, line in enumerate(open('A-large.in')):
	if ln == 0:
		continue
	ex = line.split()
	print "Case #%d: %s" % (ln, solve(ex[0], int(ex[1])))
