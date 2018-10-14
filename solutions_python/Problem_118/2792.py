import math

def isFair(n):
	string = str(n)
	for i in xrange(len(string) / 2):
		if string[i] != string[len(string) - i - 1]:
			return False
	return True

def isFairAndSquare(n):
	if not isFair(n):
		return False
	root = math.sqrt(n)
	if root % 1 != 0:
		return False
	return isFair(math.trunc(root))


f = open('input', 'r')
numTests = int(f.readline())
outputs = []

for n in range(1, numTests + 1):
	l = f.readline().split(' ')
	a = int(l[0])
	b = int(l[1])
	count = 0
	for i in range(a, b + 1):
		if isFairAndSquare(i):
			count += 1
	outputs += ["Case #{0}: {1}".format(n, count)]

for o in outputs:
	print o