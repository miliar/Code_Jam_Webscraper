import sys

def split(better, u):
	while u > 0.0000001:
		m = min(better)
		n = 0
		idx = 0
		st = []
		secondMin = 1
		for elem in better:
			if elem == m:
				n += 1
				st.append(idx)
			elif secondMin > elem:
				secondMin = elem
			idx += 1
		if (secondMin - m) * n < u:
			for i in st:
				better[i] += secondMin - m
			u -= (secondMin - m) * n
		else:
			give = u / n
			for i in st:
				better[i] += give
			u = 0
	return better


def _main():
	n, k = raw_input().split(' ')
	n = int(n)
	k = int(k)
	u = float(raw_input())
	prob = raw_input().split(' ')
	better = []
	other = []
	l = 0
	for elem in prob:
		e = float(elem)
		if l < k:
			better.append(e)
			l += 1
		else:
			m = min(better)
			if e > m:
				other.append(m)
				better[better.index(m)] = e
			else:
				other.append(e)
	better = split(better, u)
	prob = 1
	for elem in better:
		prob *= elem
	print '{:.7f}'.format(prob)

nbTest = int(raw_input())
for i in range(1, nbTest + 1):
	sys.stderr.write(str(i) + "\n")
	print "Case #"+ str(i) + ":",
	_main()