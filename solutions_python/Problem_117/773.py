import sys

def trimRow(row):
	highest = max(row)
	if highest < 0:
		return row

	newrow = row[:]

	i = 0
	for _x in newrow:
		if _x == highest:
			newrow[i] = -highest
		elif -highest > _x:
			return row
		i = i + 1
	return newrow

def missedASpot(matrix):
	for _row in matrix:
		for _col in _row:
			if _col > 0:
				return True
	return False

if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	t = int(f.readline())
	for _t in xrange(t):
		s = f.readline().split()

		n = int(s[0])
		m = int(s[1])

		rows = list()

		for _n in xrange(n):
			s = f.readline().split()

			cols = list()
			for _m in xrange(m):
				cols.append(int(s[_m]))
			rows.append(cols)

		keeptrying = True
		while keeptrying:
			keeptrying = False

			i = 0
			for _row in rows:
				newrow = trimRow(_row)
				if newrow != _row:
					keeptrying = True

				rows[i] = newrow
				i = i + 1

		transverse = zip(*rows)
		i = 0
		rows = list()
		for _trows in transverse:
			newrow = list()
			for _x in xrange(len(_trows)):
				newrow.append(_trows[_x])
			rows.append(newrow)
			i = i + 1

		keeptrying = True
		while keeptrying:
			keeptrying = False

			i = 0
			for _row in rows:
				newrow = trimRow(_row)
				if newrow != _row:
					keeptrying = True

				rows[i] = newrow
				i = i + 1

		if missedASpot(rows):
			print "Case #%d: NO" % (_t + 1)
		else:
			print "Case #%d: YES" % (_t + 1)
