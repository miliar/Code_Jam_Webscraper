from sys import stdin
from math import sqrt, ceil, floor

def is_palindrome(x):
	stx = str(x)
	lx = len(stx)

	if lx % 2 == 0:
		prestx = stx[0:(lx/2)]
		sufstx = stx[(lx/2):]
	else:
		prestx = stx[0:(lx/2)]
		sufstx = stx[(lx/2+1):]

	if prestx == sufstx[::-1]:
		return True
	return False


T = int(stdin.readline())

for case in range(1, T+1):
	A, B = map(int, stdin.readline().split())

	low = int(ceil(sqrt(A)))
	high = int(floor(sqrt(B)))
	count = 0
	for i in range(low, high+1):
		if not is_palindrome(i):
			continue
		if not is_palindrome(i**2):
			continue
		count += 1

	print "Case #%d: %d" % (case, count)