# -*- coding: utf-8 -*-

def load_input():
	T = int(raw_input())  # read a line with a single integer
	N_list = []
	for i in xrange(T):
		N_list.append(int(raw_input()))
	return N_list
	# print("Case #{}: {} {}".format(i, n + m, n * m))
	# check out .format's specification for more formatting options


def solve(N):
	for i in xrange(len(str(N))):
		strN = str(N)
		# print N
		zeros, last_n, low_digits = True, 9, 0
		for d, n in enumerate(reversed(strN)):
			n = int(n)
			# print d, n,
			if last_n < n:
				if zeros:
					N = N -1
				else:
					# print N, last_n, d, 
					# N = N - ((last_n+1) * (10 ** (d-1)))
					N = N - (low_digits+1)
				break
			last_n = n
			low_digits = low_digits + n * (10 ** d)
			# print N, low_digits
			if n:
				zeros = False
		else:
			# print N, zeros
			return N


def main():
	N_list = load_input()
	for i, N in enumerate(N_list):
		n = solve(N)
		print 'Case #%(i)d: %(n)d' % {'i': i+1, 'n': n}


if __name__ == '__main__':
	main()
