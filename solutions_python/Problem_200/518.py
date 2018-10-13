import numpy as np
def prettify(L):
	if len(L) == 1:
		return L
	n = len(L)
	"""
	if L[0] == 1 and np.all([L[i] == 0 for i in xrange(1, n)]):
		return [9]*(n-1)
	"""
	i = 0
	while L[i] <= L[i + 1]:
		i += 1
		if i == n - 1:
			return L
	while not L[i] <= L[i + 1]:
		L[i] -= 1
		i -= 1
		if i == -1:
			break
	i += 2
	for j in xrange(i, n):
		L[j] = 9
	if L[0] == 0:
		return L[1:]
	return L

def win(inp, outp):
	lines = open(inp, 'rb').readlines()
	res = []
	for line in lines[1:]:
		if line[-1] == '\n':
			line = line[:-1]
		res.append("".join(map(str, prettify(map(int, line)))))
	out = []
	for i in xrange(len(res)):
		out.append('Case #{}: {}'.format(str(i + 1), res[i]))
	f = open(outp, 'wb')
	f.write('\n'.join(out))
	f.close()

win("/Users/Dan/Desktop/codejam/Bi2.in", '/Users/Dan/Desktop/codejam/Bo2.txt')