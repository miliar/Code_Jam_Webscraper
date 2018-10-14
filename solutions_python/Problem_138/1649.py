fo = open('D-large.out', 'w')
data = open('D-large.in').readlines()
print (data)
num = int(data[0].strip())
for z in range(1, num + 1):
	n = data[(z - 1) * 3 + 2].split()
	k = data[(z - 1) * 3 + 3].split()
	for i in range(len(n)):
		n[i] = float(n[i])
		k[i] = float(k[i])
	n = sorted(n, reverse=True)
	k = sorted(k, reverse=True)
	j = 0
	b = 0
	for i in range(len(n)):
		if n[i] > k[j]:
			b += 1
		else:
			j += 1
	
	a = 0
	idx = 0
	for i in range(len(n)):
		for j in range(idx, len(n)):
			idx += 1
			if n[i] > k[j]:
				a += 1
				j += 1
				break
	
	print (n)
	print (k)
	s = 'Case #%d: %d %d' % (z, a, b)
	print (s)
	fo.write(s + '\n')
		