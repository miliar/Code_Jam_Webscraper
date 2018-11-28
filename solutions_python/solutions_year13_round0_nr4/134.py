def search(k, c, seq):
	if len(c) == 0:
		return True
	
	k_has = [] + k
	for cc in c:
		k_has += ck[cc]
	for cc in c:
		if k_has.count(keys[cc]) <= ck[cc].count(keys[cc]):
			return False
	for cc in c:
		if keys[cc] in k_has:
			k_has.remove(keys[cc])
		else:
			return False
	
	for cc in c:
		if keys[cc] in k:
			seq.append(cc)
			k2 = [] + ck[cc] + k
			k2.remove(keys[cc])
			c2 = [] + c
			c2.remove(cc)
			if search(k2, c2, seq):
				return True
			seq.pop()

	return False
	
fin = open('d.in', 'r')
fout = open('d.out', 'w')

n = int(fin.readline().strip())

for i in range(1, n+1):
	print '* ', i
	p1, p2 = fin.readline().strip().split(' ')
	k = fin.readline().strip().split(' ')
	k = [int(x) for x in k]
	c = [x for x in range(1, int(p2)+1)]
	kc = {}
	ck = {}
	keys = {}
	for j in range(1, int(p2)+1):
		p = fin.readline().strip().split(' ')
		p = [int(x) for x in p]
		if not p[0] in kc:
			kc[p[0]] = []
		keys[j] = p[0]
		kc[p[0]].append(j)
		ck[j] = p[2:]
	
	seq = []
	print k, '\n', c, '\n', kc, '\n', ck, '\n'
	if search(k, c, seq):
		fout.write('Case #%d: %s\n' % (i, ' '.join([str(x) for x in seq])))
	else:
		fout.write('Case #%d: IMPOSSIBLE\n' % i)
		
fout.close()