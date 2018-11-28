from queue import Queue
f = open('A-small-attempt0.in', 'r')
g = open('data.out', 'w')

t = int(f.readline())
for i in range(0, t):
	q = Queue()
	s, x = f.readline().split()
	ss = '+' * len(s)
	q.put(s)
	d = {
		s: 0,
	}
	ok = False
	while not q.empty():
		y = q.get()
		if(y == ss):
			g.write('Case #' + str(i + 1) + ': ' + str(d[y]) + '\n')
			ok = True
			break
		for j in range(len(y) - int(x) + 1):
			l = list(y)
			for k in range(j, j + int(x)):
				if l[k] == '-':
					l[k] = '+'
				else:
					l[k] = '-'
			z = "".join(l)
			if z not in d:
				q.put(z)
				d[z] = d[y] + 1
	if not ok:
		g.write('Case #' + str(i + 1) + ': ' + 'IMPOSSIBLE\n')
f.close()
g.close()