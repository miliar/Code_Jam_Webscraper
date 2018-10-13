# Ominous Omino

import fileinput

def solve(x, r, c):
	n = r * c

	if x == 1: return True

	if x == 2: return n % 2 == 0

	if x == 3:
		if n % 3 != 0: return False
		if r == 1 or c == 1: return False
		return True

	if x == 4:
		if n % 4 != 0: return False
		if n == 4 or n == 8: return False
		return True

f = fileinput.input()
for t in range(int(f.readline().rstrip())):
	x, r, c = map(int, f.readline().rstrip().split(' '))
	z = solve(x, r, c)
	print('Case #%s: %s' % (t + 1, 'GABRIEL' if z else 'RICHARD'))
