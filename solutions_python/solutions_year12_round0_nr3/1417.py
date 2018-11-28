def greater_eq(a, b, eq):
	if a == "":
		return eq

	a0 = int(a[0])
	b0 = int(b[0])
	if (a0 > b0):
		return True
	if (a0 < b0):
		return False
	else:
		return greater_eq(a[1:], b[1:], eq)

def check(n, m, A, B):
	if greater_eq(n, m, True) or greater_eq(A, n, False) or greater_eq(m, B, False):
		return False
	return True

def rotate(n, A, B):
	pairs = []
	n_s = str(n)

	length = len(n_s)
	for i in range(-1, -length, -1):
		m_s = n_s[i:] + n_s[:length+i]
		m = int(m_s)
		if check(n_s, m_s, str(A), str(B)):
			pairs.append((n, m))
	return pairs

if __name__ == "__main__":
	input = file("C-small.in").read().strip().split('\n')
	output = open("C-small.out", "w")

	cases = int(input[0])
	for i in range(0, cases):
		line = input[i+1].split()
		A = int(line[0])
		B = int(line[1])
		pairs = set()
		for n in range (A, B+1):
			res = rotate(n, A, B)
			for pair in res:
				pairs.add(pair)
		output.write("Case #{0}: {1}\n".format(i+1, len(pairs)))
	output.close()

