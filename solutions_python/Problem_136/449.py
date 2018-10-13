#! /usr/bin/python

def solve(input_data):
	c, f, x = input_data

	r = 2.0

	if x <= c:
		return x/r

	t = 0.0
	d = 0.0

	while d < x:
		if d < c:
			t = t + (c - d) / r
			d = c
		else:
			if (x - d) / r <= (x - d + c) / (r + f):
				t = t + (x - d) / r
				d = x
				break
			r = r + f
			d = d - c
	return t

def read_input():
	return map(float, raw_input().split())

def main():
	T = int(raw_input())
	for t in xrange(T):
		print "Case #%d: %.7f" % (t + 1, solve(read_input()))

if __name__ == "__main__":
	main()