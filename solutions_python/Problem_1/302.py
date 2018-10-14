import os, sys

class Case:
	def __init__(self):
		self.caseid = 0
		self.engines = []
		self.queries = []
	def switches(self):
		s = 0
		q = self.queries[:]
		q.reverse()
		d = dict()
		for x in self.engines:
			d[x] = 0
		while len(q) > 0:
			t = q.pop()
			d[t] += 1
			f = False
			for y in d.keys():
				if d[y] == 0:
					f = True
			if not f:
				for y in d.keys():
					d[y] = 0
				s += 1
				q.append(t)
		return s

	def __str__(self):
		return str(self.caseid)


if __name__ == "__main__":
	ncases = int(sys.stdin.readline())
	cases = []
	for x in range(ncases):
		c = Case()
		neng = int(sys.stdin.readline())
		for y in range(neng):
			c.engines.append(sys.stdin.readline())
		nque = int(sys.stdin.readline())
		for z in range(nque):
			c.queries.append(sys.stdin.readline())
		c.caseid = x + 1
		cases.append(c)
	for x in cases:
		print "Case #%d: %d" % (x.caseid, x.switches())
