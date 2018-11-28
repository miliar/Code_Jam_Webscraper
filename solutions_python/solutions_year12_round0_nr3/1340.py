import cj

def parse(reader):
	A = reader/int
	B = reader/int
	return A, B

def rewind(str):
	return str[1:] + str[0]

def generate_all(A, B):
	pairs = []
	for i in xrange(B, A - 1, -1):
		s = str(i)
		l = len(s) - 1
		for j in xrange(l):
			s = rewind(s)
			u = int(s)
			if u < i and u >= A:
				pairs.append((i, u))
	return set(pairs)

def solve(A, B):
	num = 0
	for (i, j) in set_of_everything:
		if i >= A and i <= B and j >= A and j <= B:
			num += 1
	return num

set_of_everything = generate_all(1, 2000000)

cj.jam(parse, solve)