import sys

sinfile = sys.argv[1]
soutfile = sinfile[:-2] + 'out'

finfile = open(sinfile)
foutfile = open(soutfile, 'w')


n = int(finfile.readline().strip())

def diff(arr):
	init = 1
	o = []
	for x in arr:
		o.append(abs(x-init))
		init = x
	return o

for i in range(1, n+1):
	l = iter(finfile.readline().strip().split(' '))
	combs = {}
	for x in range(int(l.next())):
		y = l.next()
		ab = y[:2]
		r = y[2]
		combs[ab] = r
		ab = list(ab)
		ab.reverse()
		combs[''.join(ab)] = r
		pass
	ops	= {}
	for x in range(int(l.next())):
		y = l.next()
		ops[y[0]] = y[1]
		ops[y[1]] = y[0]
		pass

	elemnum = l.next()
	temp = []
	inputlist = l.next()
	for s in inputlist:
		if len(temp) > 0:
			last = temp[-1]
			if combs.has_key(last+s):
				#combined!
				temp.pop()
				temp.append(combs[last+s])
				continue
		try:
			temp.index(ops[s])
			temp = []
		except:
			temp.append(s)
	ans = temp

	print >> foutfile, ('Case #%d: %s' % (i, ans)).replace("'", '')