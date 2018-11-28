from sys import stdin
t = int(stdin.readline())
for i in range(t):
	line = stdin.readline().split()
	n = int(line[0])
	s = int(line[1])
	p = int(line[2])
	r = 0;
	for j in range(n):
		x = int(line[j + 3]);
		a = x / 3;
		b = x % 3;
		min = a + (b + 1) / 2
		max = a + b / 2 + 1
		if x == 0:
			 max = 0
		if min >= p:
			r += 1
		elif max >= p and s > 0:
			r += 1
			s -= 1
	print 'Case #' + str(i + 1) + ': ' + str(r)
