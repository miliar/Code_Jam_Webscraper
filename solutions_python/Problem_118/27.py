from itertools import *

a = []

ct = 0
# even numbered
for j in range(1,5):
	for x in combinations(range(25), j):
		ct += 1
		q = 25 * ['0']
		for y in x:
			q[y] = '1'

		s = ''.join(q[x[0]:])
		s += s[::-1]
		a.append(s)

for j in range(0,25):
	a.append('2'+ (2*j)*'0'+'2')
#odd numbered

for j in range(24):
	a.append('2'+(2*j+1)*'0'+'2')
	a.append('2'+j*'0'+'1' + j*'0'+ '2')
	a.append('1'+j*'0'+'2' + j*'0'+ '1')

for j in range(1,5):
	for x in combinations(range(24), j):
		q = 24 * ['0']
		for y in x:
			q[y] = '1'

		s = ''.join(q[x[0]:])
		a.append(s + '0' + s[::-1])
		a.append(s + '1' + s[::-1])


for x in combinations(range(24), 2):
		q = 24 * ['0']
		for y in x:
			q[y] = '1'

		s = ''.join(q[x[0]:])
		a.append(s + '2' + s[::-1])


def cc(x,y):
	if len(x) != len(y):
		return len(x) - len(y)
	if x < y:
		return -1
	if x > y:
		return 1
	return 0

a += ['1','2','3']
a.sort(cmp=cc)

b = [long(x)*long(x) for x in a]

T = input()

for case in range(T):
	x = raw_input().split()
	[A,B] = [long(y) for y in x]
	ct = 0
	for y in b:
		if A <=y <= B:
			ct+= 1
	print "Case #%d: %d" % (case + 1, ct)