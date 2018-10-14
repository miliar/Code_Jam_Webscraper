import sys
sys.stdin = open('B.txt', 'r')
sys.stdout = open('B.out', 'w')

def step(x):
	for i, (c1, c2) in enumerate(zip(x[:-1], x[1:])):
		if int(c1) > int(c2):
			return x[:i] + str(int(c1) - 1) + (len(x) - 1 - i) * '9'
	return x

def solve(x):
	x2 = step(x)
	while x != x2:
		x = x2
		x2 = step(x)
	return x.lstrip('0')

T = input()
nums = [raw_input() for _ in range(T)]
print '\n'.join('Case #{}: {}'.format(i + 1, solve(n)) for i, n in enumerate(nums))
