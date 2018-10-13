# Code Jam 2009
# Round 1C - C

import sys
import ctypes
import string
import itertools

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

@memoized
def coin_count(a, b):
	# a is the list of cells (empty/full as False/True)
	# b is the release order
	if len(b) == 0:
		return 0
	j = b[0]
	n = 0
	# first go up
	for i in xrange(j+1, len(a)):
		if a[i]:
			n += 1
		else:
			break
	for i in xrange(j-1, -1, -1):
		if a[i]:
			n += 1

		else:
			break
	a[j] = False
	return n + coin_count(a, b[1:])



def print_cases(cases):
	for n in xrange(len(cases)):
		print "Case #" + str(n+1) + ": " + str(cases[n])

def main():
	input_N = int(sys.stdin.readline().rstrip())
	cases = []
	for N in xrange(input_N):
		line = sys.stdin.readline().split()
		input_P = int(line[0])
		input_Q = int(line[1])

		release = []
		line = sys.stdin.readline().split()
		for p in line:
			release.append((int(p) - 1))

		#just brute force it!
		perm = itertools.permutations(release)
		lowest = None
		for i in perm:
			l = [True] * input_P
			if lowest is not None:
				lowest = min(coin_count(l, i), lowest)	
			else:
				lowest = coin_count(l, i)
		cases.append(lowest)

	print_cases(cases)


if __name__ == '__main__':
	main()



