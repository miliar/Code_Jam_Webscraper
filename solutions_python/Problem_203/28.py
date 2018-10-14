def span(row):
	last = '?'
	ret = []
	for c in row:
		if c != '?':
			last = c
		ret.append(last)
	last = '?'
	for i, c in enumerate(reversed(row), 1):
		if c != '?':
			last = c
		if ret[-i] == '?':
			ret[-i] = last
	return ret


for x in range(1, int(input()) + 1):
	R, C = map(int, input().split())
	s = []
	for r in range(R):
		row = input()
		s.append(span(row))
	for c in range(C):
		col = ''
		for r in range(R):
			col += s[r][c]
		ncol = span(col)
		for i, ncell in enumerate(ncol):
			s[i][c] = ncell

	print('Case #%d:' % x)
	print('\n'.join(''.join(x) for x in s))
