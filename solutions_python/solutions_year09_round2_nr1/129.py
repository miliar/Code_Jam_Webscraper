# Code Jam 2009
# Round 1B - A

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

class dtree(object):
	def __init__(self):
		self.l = None
		self.r = None
		self.weight = 0
		self.char = ''
	def parse(self, s, rem=''):
		if len(s) == 0:
			return ''
		if len(rem) == 0:
			if s[0] == '(':					
				return self.parse(self.add_token('(', s[1:]))
			elif s[0] == ')':
				return s[1:] #done
			elif s[0] == ' ':
				return self.parse(s[1:])
			elif s[0] in string.digits or s[0] == '.':
				return self.parse(s[1:], s[0])
			else: #alpha
				return self.parse(s[1:], s[0])
		if s[0] in string.digits or s[0] == '.':
			return self.parse(s[1:], rem + s[0])
		elif s[0] in string.letters:
			return self.parse(s[1:], rem + s[0])
		else:
			return self.parse(self.add_token(rem, s))		


	def add_token(self, t, s):
		if t == '(':
			if self.l is None:
				self.l = dtree()
				return self.l.parse(s)
			else:
				self.r = dtree()
				return self.r.parse(s)
		elif t[0] in string.digits:
			self.weight = float(t)
			return s
		else:
			self.char = t
			return s

	def find(self, f, c=1):
		c *= self.weight


		if len(f) == 0:
			if self.r is not None:
				return self.r.find(f, c)
			else:
				return c

		if self.char in f:
			if self.l is not None:
				return self.l.find(f, c)
			else:
				return c

		if self.r is not None:
			return self.r.find(f, c)
		else:
			return c


def print_cases(cases):
	for n in xrange(len(cases)):
		print "Case #" + str(n+1) + ": " 
		for case in cases[n]:
			print '%.7f' % case

def main():
	input_N = int(sys.stdin.readline().rstrip())
	cases = []
	for N in xrange(input_N):
		cases.append([])
		input_l = int(sys.stdin.readline().rstrip())

		dt = dtree()
		first = True
		items = ''
		for l in xrange(input_l):
			input_x = sys.stdin.readline().rstrip()
			items += input_x

		items = items[1:] # remove first parens
		dt.parse(items)
		input_a = int(sys.stdin.readline().rstrip())

		for a in xrange(input_a):
			ani = sys.stdin.readline().split()
			name = ani[0]
			input_n = int(ani[1])
			features = []
			for n in xrange(input_n):
				features.append(ani[n + 2])

			cute = dt.find(features)

			cases[N].append(cute)
		

	print_cases(cases)


if __name__ == '__main__':
	main()

