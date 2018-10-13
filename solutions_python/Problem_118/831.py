import math
import sys

def ifPalindrome(ns):
	l = len(ns)
	for i in range(l/2):
		if ns[i] != ns[l-i-1]:
			return False
	return True

def ifFair(n):
	ns = str(n)
	return ifPalindrome(ns)


def ifSquareOfFairAndSquare(n):
	if ifFair(n) and ifFair(n*n):
		return True
	return False

if __name__ == "__main__":
	'''
	max_of_number = 10**14
	max_of_square = int(math.sqrt(max_of_number))

	s = []

	n = 1
	while n <= max_of_square:
		if ifSquareOfFairAndSquare(n):
			s.append(n*n)
		n += 1

	print s
	'''
	s = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

	
	args = sys.argv[1:]
	fname = args[0]
	f = open(fname)

	T = f.readline()
	T = int(T)

	for t in range(T):
		case_number = t + 1

		line = f.readline().strip()
		line = line.split(" ")
		A = int(line[0])
		B = int(line[1])

		c = 0
		for e in s:
			if A <= e and e <= B:
				c += 1
			if e > B:
				break

		print "Case #%d: %d" % (case_number, c)
	





