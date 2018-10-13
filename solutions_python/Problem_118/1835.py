# 00:52

import math

def palindrome(n):
	return str(n) == str(n)[::-1]

def doit(a,b):
	x = int(math.sqrt(a))
	result = 0
	while True:
		if x*x >= a and palindrome(x):
			if x*x > b:
				return result
			if palindrome(x*x):
				result += 1
		x += 1

def main():
	# fp = open('c.in')
	fp = open('C-small-attempt0.in')

	for case in xrange(int(fp.readline())):
		a,b = map(int, fp.readline().split())

		result = doit(a,b)

		print 'Case #{0}: {1}'.format(case+1, result)


if __name__ == "__main__":
	main()
