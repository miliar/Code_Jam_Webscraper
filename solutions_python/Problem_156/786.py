# Infinite House of Pancakes

import fileinput
from math import floor, ceil

def solve(a):
	if max(a) <= 3: return max(a)

	a1 = list(a)
	x = a1[0]
	a1[0] = ceil(x / 2)
	if x // 2: a1.append(x // 2)
	a1.sort(reverse=True)

	a2 = list(a)
	x = a2[0]
	a2[0] = round(2 * x / 3)
	if round(x / 3): a2.append(round(x / 3))
	a2.sort(reverse=True)	

	a3 = [x - 1 for x in a if x > 0]
	return 1 + min(solve(a1), solve(a2), solve(a3))

f = fileinput.input()
for t in range(int(f.readline().rstrip())):
	n = int(f.readline().rstrip())
	a = list(map(int, f.readline().rstrip().split(' ')))
	a.sort(reverse=True)
	z = solve(a)
	print('Case #%s: %s' % (t + 1, z))
