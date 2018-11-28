import pprint

def create_table(surprising=False):
	d = 2 if surprising else 1
	table = {}
	for i in xrange(0, 11):
		r = xrange(max(0, i - d), min(i + d, 11))
		for j in r:
			for k in r:
				s = i + j + k
				m = max([i, j, k, table.get(s, 0)])
				table[s] = m
	return table

def count(surprising, p, notes, m, ms):
	c = 0
	for n in reversed(sorted(notes)):
		if m[n] >= p:
			c += 1
		elif ms[n] >= p and surprising > 0:
			c += 1
			surprising -= 1
		else:
			break
	return c

def solve(name, m, ms):
	with open (name) as f:
		d = f.readlines()
	with open (name.replace('.in', '.out'), 'w') as o:
		for i, line in enumerate(d[1:]):
			line = map(int, line.strip().split(' '))
			N = line[0]
			S = line[1]
			p = line[2]
			T = line[3:]
			assert len(T) == N
			o.write("Case #%d: %d\n" % (i + 1, count(S, p, T, m, ms)))

if __name__ == '__main__':
	m = create_table()
	ms = create_table(True)
	solve('B-large.in', m, ms)
