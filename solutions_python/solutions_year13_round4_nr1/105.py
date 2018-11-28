'''
CodeJam 2013 Round 2
Problem A: Ticket Swapping
Author: Jon Eisen

This solution uses [pycodejam](http://github.com/yanatan16/pycodejam).
'''
from codejam import CodeJam, parsers
from codejam.helpers import memoize

modulo = 1000002013

@memoize
def cost(n, stops):
	return sum((n-k for k in range(stops))) % modulo

def exp_value(n, traffic):
	return sum((p * cost(n, e-o) for o, e, p in traffic)) % modulo

def swap_value(n, traffic):
	pipeline = [0 for _ in range(n-1)]
	for o, e, p in traffic:
		for k in range(o, e):
			pipeline[k-1] += p

	print pipeline

	return pipeline_value(n, pipeline)

def split(arr, val):
	aarr = []
	li = 0
	for i, a in enumerate(arr):
		if a == val:
			aarr += [arr[li:i]]
			li = i + 1

	aarr += [arr[li:]]
	return aarr

def pipeline_value(n, pipeline):
	# find contiguous segments of users
	value = 0
	spipe = split(pipeline, 0)
	for pipe in spipe:
		if len(pipe):
			m = min(pipe)
			pipe = [p - m for p in pipe]
			value += m * cost(n, len(pipe))
			value += pipeline_value(n, pipe)

	return value

def solve(n, traffic):
	return (exp_value(n, traffic) - swap_value(n, traffic)) % modulo

@parsers.iter_parser
def parse(nxt):
	ints = lambda: [int(x) for x in nxt().split()]
	n, m = ints()
	traffic = [ints() for _ in range(m)]
	return n, traffic

if __name__ == "__main__":
	CodeJam(parse, solve).main()