import math

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def calculate(a, b):
	powers = []
	for i in range(42):
		powers.append(2 ** i)

	g = gcd(a, b)
	a = int(round(a / g))
	b = int(round(b / g))

	if b not in powers:
		return None

	for n in range(len(powers)):
		if a / b >= 1 / powers[n] - 0.00000000001:
			return n

n = int(input())
for i in range(n):
	a, b = [int(x) for x in input().split('/')]
	r = calculate(a, b)
	if r is None: print('Case #%s: impossible' % (i + 1))
	else: print('Case #%s: %s' % (i + 1, r))