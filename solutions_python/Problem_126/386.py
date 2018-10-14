import sys
from multiprocessing import Pool


def solve(arg):
	name = arg[0]
	n = arg[1]
	
	nv = 0
	c = 0
	i = 0
	pairs = set()
	while (i < len(name)):
		if isC(name[i]):
			c += 1
			if (c == n):
				nv += noSubstrings(len(name), i-c+1, i, pairs)
				c -= 1
		else:
			c = 0
		i += 1
	return nv
	
def isC(c):
	return c != 'a' and c != 'i' and c != 'o' and c != 'u' and c != 'e'
	
def noSubstrings(ll, start, end, pairs):
	print("Nos %d %d %d" % (ll, start, end))
	c = 0
	for st in range(0, start+1):
		for en in range(ll-1, end-1, -1):
			if (st, en) not in pairs:
				c += 1
				pairs.add((st, en))
	print c
	return c
	
def solvePar(args):
	p = Pool(4)
	res = p.map(solve, args)
	return res
	
	
f = open(sys.argv[1])
o = open("p1.out","w")
with f:
	with o:
		args = []
		t = int(f.readline())
		for i in range(0,t):
			line = f.readline()
			word,n = line.split(" ")
			args.append((word, int(n)))

		res = []
		for arg in args:
			res.append(solve(arg))
		i = 0
		for r in res:
			o.write("Case #%d: %s\n" % (i+1, r))
			i += 1
