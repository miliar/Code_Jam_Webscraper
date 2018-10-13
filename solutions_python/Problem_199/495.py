import numpy as np
def bitify(s):
	L = []
	for x in s:
		if x == '+':
			L.append(0)
		elif x == "-":
			L.append(1)
		else:
			assert(0), 'wat'
	return np.array(L, dtype = np.uint8)

def calc_nr(b, k):
	o = np.ones(k, dtype = np.uint8)
	c = 0
	for i in xrange(len(b) - k + 1):
		if b[i]:
			b[i:i+k] ^= o
			c += 1
	if any(b[-k:]):
		return "IMPOSSIBLE"
	else:
		return str(c)

def win(inp, outp):
	lines = open(inp, 'rb').readlines()
	res = []
	for line in lines[1:]:
		if line[-2:] == '\r\n':
			line = line[:-2]
		if line[-1:] == '\n':
			line = line[:-1]
		s, k = line.split(' ')
		k = int(k)
		res.append(calc_nr(bitify(s), k))
	out = []
	for i in xrange(len(res)):
		out.append('Case #{}: {}'.format(str(i + 1), res[i]))
	f = open(outp, 'wb')
	f.write('\n'.join(out))
	f.close()

win("/Users/Dan/Desktop/codejam/i2.in", '/Users/Dan/Desktop/codejam/o2.txt')