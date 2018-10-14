import sys

f = sys.stdin

line = f.readline()
l, d, n = [int(s) for s in line.split()]

wl = []
for d in range(d):
	wl.append(f.readline())

for n in range(1, n+1):
	p = f.readline()
	m = []
	j = 0;
	for i in range(l):
		if p[j] == '(':
			j += 1;
			w = []
			while p[j] != ')':
				w.append(p[j])
				j += 1
		else:
			w = [p[j]]
		m.append(w)
		j += 1

	v = 0
	for w in wl:
		flag = True
		for i in range(l):
			if w[i] not in m[i]:
				flag = False
				break
		if flag:
			v += 1

	print "Case #%s: %s" % (n, v)

