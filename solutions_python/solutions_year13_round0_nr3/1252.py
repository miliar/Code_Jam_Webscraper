
def squares(start):
	i = start
	while True:
		yield (i, i*i)
		i += 1

def pali(n):
	s = str(n)
	return s == s[::-1]

# for i in squares(100):
# 	print i

# 	if i[0] > 10000000000:
# 		break

from math import *

f = open("C-small-attempt0.in", 'r')

num_ranges = int(f.readline())

inp = []
for i in range(num_ranges):
	l = f.readline()

	r = l.split(' ')
	r = (int(r[0]), int(r[1]))

	inp.append(r)

for i in range(len(inp)):
	(a, b) = inp[i]

	start = int(ceil(sqrt(a)))

	sq = squares(start)
	l = []
	for (n, nsq) in sq:
		if nsq > b:
			break
		if pali(n) and pali(nsq):
			l.append((n, nsq))

	print 'Case #' + str(i + 1) + ': ' + str(len(l))