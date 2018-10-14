fo = open('A-small-1.out', 'w')
data = open('A-small-attempt0.in').readlines()
print (data)
num = int(data[0].strip())
for z in range(num):
	a = data[z * 10 + 1].strip()
	b = data[z * 10 + 6].strip()
	r1 = data[z * 10 + 1 + int(a)].split()
	r2 = data[z * 10 + 6 + int(b)].split()
	print (r1, r2)
	res = []
	for r in r1:
		print (r, r in r2)
		if r in r2:
			res.append(r)
	if len(res) == 0:
		s = 'Case #%d: Volunteer cheated!' % (z + 1)
	elif len(res) == 1:
		s = 'Case #%d: %s' % (z + 1, res[0])
	else:
		s = 'Case #%d: Bad magician!' % (z + 1)
	print (s)
	fo.write(s + '\n')
		