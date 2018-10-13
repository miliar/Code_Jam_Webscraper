import operator
from sys import stdin
from itertools import islice

def stupid_sum(candy):
	return reduce(operator.xor, candy)

def combinations(candy, sean=None, patrick=None):
	if sean==None: sean=[]
	if patrick==None: patrick=[]

	if not candy and sean and patrick and stupid_sum(sean) == stupid_sum(patrick):
		yield sum(sean)

	if candy:
		head = candy[0]
		tail = candy[1:]

		for i in combinations(tail, sean + [head], patrick):
			yield i
	
		for i in combinations(tail, sean, patrick + [head]):
			yield i

def solution(candy):
	combis = list(combinations(candy))
	if not combis: return 'NO'

	return str(max(combis))

def parse_input(inputFile):
	for line in islice(inputFile, 2, None, 2):
		yield map(int, line.split())

for test, candy in enumerate(parse_input(stdin)):
	print 'Case #%d: %s' % (test + 1, solution(candy))
