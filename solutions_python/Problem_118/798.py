#!/usr/bin/env python

def get_square(n):

	h = n % 16

	if h == 0 or h == 1 or h == 4 or h == 9:
		t = int(n ** 0.5 + 0.5)
		if t * t == n:
			return t

	return None


def ispalindrome(n):

	str_n = str(n)
	len_n = len(str_n)

	for i in xrange(len_n / 2):
		if str_n[i] != str_n[len_n - i - 1]:
			return False

	return True


def main():

	cache = {}

	test_data = None
	with open('input', 'r') as f:
		test_data = f.read()

	test_data = test_data.split('\n')

	num_test = int(test_data[0])
	for test in xrange(num_test):
		a, b = map(int, test_data[test + 1].split(' '))

		counter = 0
		result = []
		for i in xrange(a, b + 1):
			if i in cache:
				counter += 1
			else:
				if ispalindrome(i):
					sqrt = get_square(i)
					if sqrt is not None and ispalindrome(sqrt):
						cache[i] = True
						counter += 1

		print 'Case #%s: %s' % (test + 1, counter)

if __name__ == "__main__":
	main()