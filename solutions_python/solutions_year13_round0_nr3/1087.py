#!/usr/bin/env python
#
# Luke Southam <luke@devthe.com>
# GCJ Problem C. Fair and Square
#

from math import sqrt, ceil

square = lambda n: n**2
squares = lambda min_, max_: map(square, filter(is_palindrome, range(int(ceil(sqrt(min_))), int(sqrt(max_)) + 1)))
is_palindrome = lambda n: str(n) == str(n)[::-1]

T = int(raw_input())

for test in xrange(T):
	min_, max_ = map(int, raw_input().split())

	results = filter(is_palindrome, squares(min_, max_))

	print "Case #%i: %i" % (test + 1, len(results))
