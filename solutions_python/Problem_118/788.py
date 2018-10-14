import sys

from math import log, floor, ceil, sqrt
from itertools import takewhile, imap, count

def isqrt(x):
    """
    From http://code.activestate.com/recipes/577821-integer-square-root-function/
    """
    orig = x
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
	    assert (x + 1) * (x + 1) > orig
            return x
        x = y

def is_palindrome(n):
	str_n = str(n)
	h_l = (1 + len(str_n)) / 2
	return str_n[0:h_l] == str_n[-1:-1 - h_l:-1]

def parse_case(inp):
	a, b = map(long, inp.readline().split())
	
	r_a, r_b = map(isqrt, (a, b))
	tot = 0
	x = r_a
	while x * x < a:
		x += 1
	while x <= r_b:
		if is_palindrome(x) and is_palindrome(x * x) and x * x <= b:
			tot += 1
		x += 1
	return tot

	
def parse(fileName):
	results = []
	with open(fileName) as f:
		cases = int(f.readline())
		for i in range(cases):
			results.append(parse_case(f))

		next_line = f.readline()
		assert "" == next_line, "Unexpected line: %s" % next_line
	return results

if __name__ == "__main__":
	for (i, result) in enumerate(parse(sys.argv[1])):
		print "Case #%d: %s" % (i + 1, result)
