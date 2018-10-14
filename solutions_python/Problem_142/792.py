import collections
import functools

class memoized(object):
	'''Decorator. Caches a function's return value each time it is called.
	If called later with the same arguments, the cached value is returned
	(not reevaluated).
	'''
	def __init__(self, func):
		self.func = func
		self.cache = {}
	def __call__(self, *args):
		if not isinstance(args, collections.Hashable):
			raise Exception("arguments musht be hashable")
			return self.func(*args)
		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value
	def __repr__(self):
		'''Return the function's docstring.'''
		return self.func.__doc__
	def __get__(self, obj, objtype):
		'''Support instance methods.'''
		return functools.partial(self.__call__, obj)
		
import sys

input = open(sys.argv[1], "r").readlines()#[1:]
output = open(sys.argv[2], "w")

def parse(lines):
	def inner_parse():
		line = (yield None)
		while True:
			n = int(line[0])
			words = []
			for i in range(n):
				line = (yield None)
				words.append(line[0])
			line = (yield words)
		
	parser = inner_parse()
	next(parser)
	#import pdb; pdb.set_trace()
	for raw_line in lines:
		line = raw_line.strip().split(" ")
		result = parser.send(line)
		if not result is None:
			yield result
	
def find_base(word):
	# break into sequences, then return their lengths.
	runs = []
	lengths = [1]
	for (last_letter, current_letter) in zip(word[:-1], word[1:]):
		if not current_letter == last_letter:
			runs.append(last_letter)
			lengths.append(1)
		else:
			lengths[-1] += 1

	runs.append(word[-1])

	return zip(runs, lengths)


def equal(base1, base2):
	if not len(base1) == len(base2):
		#import pdb; pdb.set_trace()
		return False

	for (pair1, pair2) in zip(base1, base2):
		if not pair1[0] == pair2[0]:
			return False

	return True

def solve(words):
	bases = [list(find_base(word)) for word in words]
	for (last, current) in zip(bases[:-1], bases[1:]):
		if not equal(last, current):
			return "Fegla Won"

	#max_lengths = [max(map(lambda x: x[index][1], bases)) for index in range(len(bases[0]))]
	avg_lengths = [round(sum(map(lambda x: x[index][1], bases))/len(bases)) for index in range(len(bases[0]))]
	diff_lengths = [sum(map(lambda x: abs(x[index][1]-avg_lengths[index]), bases)) for index in range(len(bases[0]))]

	return sum(diff_lengths)
		
for (i, words) in enumerate(parse(input[1:])):
	#import pdb; pdb.set_trace()
	result = solve(words)
	#result = words
	print("Case #" + str(i+1) + ": " + str(result))
	output.write("Case #" + str(i+1) + ": " + str(result) + "\n")