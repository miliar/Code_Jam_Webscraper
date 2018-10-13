# Code Jam 2009
# Round 1C - A

import sys
import ctypes
import string

class memoized(object):
	''' Just a templated memoizer in case I need it :) 
	Just use @memoized before a function to make use of it.'''
	def __init__(self, func):
		self.func = func
		self.cache = {}
	def __call__(self, *args):
		try:
			return self.cache[args]
		except KeyError:
			self.cache[args] = value = self.func(*args)
			return value
		except TypeError:
			return self.func(*args)
	def __repr__(self):
		return self.func.__doc__


def print_cases(cases):
	for n in xrange(len(cases)):
		print "Case #" + str(n+1) + ": " + str(cases[n])

def main():
	input_T = int(sys.stdin.readline().rstrip())
	cases = []
	for T in xrange(input_T):
		s = sys.stdin.readline().rstrip()
		digits = {}
		n = 1
		for c in s:
			if c in digits:
				continue
			if n == 1:
				digits[c] = 1
				n = 0
			elif n == 0:
				digits[c] = 0
				n = 2
			else:
				digits[c] = n
				n += 1
		l = len(s) - 1
		b = max(len(digits), 2)
		x = 0
		for c in s:
			x += digits[c] * (b ** l)
			l -= 1

		cases.append(x)

	print_cases(cases)


if __name__ == '__main__':
	main()


