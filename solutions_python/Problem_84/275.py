def solve():
	for r in xrange(R - 1):
		for c in xrange(C - 1):
			if inp[r][c] == '#' and inp[r + 1][c + 1] == '#' and inp[r][c+1] == '#' and inp[r+1][c] == '#':
				inp[r][c] = '/'
				inp[r+1][c] = '\\'
				inp[r][c+1] = '\\'
				inp[r+1][c+1] = '/'
	possible = len([1 for row in inp for char in row if char == '#']) == 0
	if possible:
		return "\r\n".join(map(lambda x: "".join(x), inp))
	else:
		return "Impossible"
	return (possible, inp)
	
T = int(raw_input())
for case in xrange(1, T + 1):
	line = raw_input().split()
	R = int(line[0])
	C = int(line[1])
	inp = [None] * R
	for r in xrange(R):
		inp[r] = list(raw_input().strip())
#	print inp
	ans = solve()
	print "Case #%d:\r\n%s" % (case, ans)