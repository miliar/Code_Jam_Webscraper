from __future__ import print_function

path = 'C-small-attempt0'
input = open(path + '.in')
output = open(path + '.out', 'w')

T = int(input.readline())
for t in range(T):
	a, b = [int(a) for a in input.readline().split(' ')]
	counter = 0
	for j in range(a, b + 1):
		c = str(j)
		v = []
		for k in range(1, len(c)):
			d = c[k:] + c[:k]
			if int(d) > j and int(d) <= b and d != c and d not in v:
				v.append(d)
				counter += 1
	print("Case #{t}: {c}".format(t = t + 1, c = counter), file = output)
