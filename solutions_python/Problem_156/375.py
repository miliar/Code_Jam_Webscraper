from sys import stdin


def tryx(x):
	r = x
	for i in l:
		if i % x == 0:
			r += i // x - 1
		else:
			r += i // x
	return r

stdin.readline()
for lno,l in enumerate(stdin, 1):
	if lno % 2 != 0:
		continue
	lno = lno / 2
	l = map(int, l.split())
	print 'Case #{}: {}'.format(lno, min(map(tryx, range(1,1001))))
