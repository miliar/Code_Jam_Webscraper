import sys
input = open('A-large.in').read().split()
input.reverse()

cases = int(input.pop())
case = 1
while cases:
	n = int(input.pop())
	k = int(input.pop())
	res = "OFF" if (k+1) % (1 << (n)) else "ON"
	print('Case #{0}: {1}'.format(case, res))
	case += 1
	