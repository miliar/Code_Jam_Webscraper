import sys

def solve(mx):

	def is_sorted(x):
		return list(str(x)) == sorted(str(x))

	while not is_sorted(mx):
		print mx
		mx -= 1

	return mx

def solve_hard(mx):

	while True:
		# find next problem
		digits = map(int, str(mx))[::-1]

		for i in xrange(len(digits)-1):
			if digits[i] < digits[i+1]:
				break
		else:
			return mx

		mx -= (mx % 10 ** i) + 1



def main():
	f = open(sys.argv[1], 'rb')
	T = int(f.readline().strip())

	ret = []
	for t in xrange(T):
		line = int(f.readline().strip())
		solve_hard(line)
		ret.append(solve_hard(line))


	for i, nums in enumerate(ret):
		print "Case #{}: {}".format(i+1, nums)

if __name__ == '__main__':
	main()