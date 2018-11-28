#! /usr/bin/python2

def getstr(l):
	ret = l[0]
	del l[0]
	return ret

def getint(l):
	return int(getstr(l))

def solve():
	inp = raw_input().split()
	c = getint(inp)
	transforms = {}
	delete = set()
	for i in range(c):
		tr = getstr(inp)
		fr = tr[:2]
		t = tr[2]
		transforms[fr]=t
		transforms[fr[1]+fr[0]]=t
	d = getint(inp)
	for i in range(d):
		d = getstr(inp)
		delete.add(d)
		delete.add(d[1]+d[0])
	n = getint(inp)
	inv = getstr(inp)
	res = []
	for x in inv:
		spell = x
		while res and (res[-1]+spell) in transforms:
			spell = transforms[res[-1]+spell]
			del res[-1]
		cl = False
		for s in res:
			if (spell + s) in delete:
				cl = True
		if cl: res = []
		else: res.append(spell)
	print str(res).replace('\'', '')

if __name__ == '__main__':
	t = input()
	for i in range(t):
		print 'Case #%d:' % (i+1),
		solve()
