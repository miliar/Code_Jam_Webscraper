i = 0
def find_min(c, f, x, p):
	m = x / p
	idx = 0
	while True:
		t = x / (p + idx * f)
		for i in range(idx):
			t += c / (2 + i * f)
		print (t)
		if t > m:
			return m
		else:
			idx += 1
			m = t
	return m

fo = open('B-small-1.out', 'w')
data = open('B-small-attempt1.in').readlines()
print (data)
num = int(data[0].strip())
for z in range(1, num + 1):
	d = data[z].split()
	c = float(d[0])
	f = float(d[1])
	x = float(d[2])
	t = find_min(c, f, x, 2)
	s = 'Case #%d: %0.7f' % (z, t)
	print (s)
	fo.write(s + '\n')
		