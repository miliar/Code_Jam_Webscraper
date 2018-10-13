import re

v = [line.strip().split() for line in open('a-small.in','r').readlines()] #large

out = open('a-small.out', 'w') #large

t = int(v[0][0])
v = v[1:]

#print(v)

dec = re.compile(r'^\s*\(\s*([01]\.\d+)(?:\s+(\w+))?\s*(\(.*\)\s*\(.*\)\s*)?\)\s*$')

p = 0

def tree(dt):
	global p
	m = dec.search(dt)
	g = m.groups()
#	print(g)
	p *= float(g[0])
	if g[2]:
		st = g[2]
		balance = 1
		i = 1
		while balance:
			if st[i] == '(':
				balance += 1
			elif st[i] == ')':
				balance -= 1
			i += 1
		fst = st[:i]
		while st[i] != '(':
			i += 1
		snd = st[i:]
#		print(fst)
#		print(snd)
		if g[1] in a:
			tree(fst)
		else:
			tree(snd)


case = 0
while case < t:
	case += 1
	l = int(v[0][0])
	dt = ' '.join([' '.join(i) for i in v[1:l + 1]])
	n = int(v[l + 1][0])
#	print(n)
	ans = v[l+2:l+n+2]
	v = v[l + n + 2:]
#	print(l)
#	print(dt)
#	print(n)
#	print(v)

	print("Case #%d:" % (case), file = out)
	for a in ans:
		a = a[2:]
		p = 1
		tree(dt)
		print("%.7f" % (p), file = out)


