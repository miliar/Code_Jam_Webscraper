
"""Google Code Jam Template Code
by Tiago Togores"""

import sys, getopt, random, math, numpy, scipy, pdb

class Data(object):
	"""data input for a problem"""
	def __init__(self):
		super(Data, self).__init__()
	def remove(self, s, k, o):
		if k == self.n:
			if self.result < 0: self.result = o
			else: self.result = min(self.result, o)
			return
		self.remove(s, k + 1, o + 1)
		self.add(s, k + 1, o + 1)
	def add(self, s, k, o):
		if k == self.n:
			if self.result < 0: self.result = o
			else: self.result = min(self.result, o)
			return
		j = 0
		while self.motes[k] >= s:
			if s == 1:
				return
			s += s - 1
			j += 1
		self.remove(s + self.motes[k], k + 1, o + j)
		self.add(s + self.motes[k], k + 1, o + j)
	def algorithm(self):
		self.motes.sort()
		self.result = -1
		self.remove(self.a, 0, 0)
		self.add(self.a, 0, 0)
		return str(self.result)

def get_data():
	data = Data()
	data.a, data.n = [int(w) for w in raw_input().split()]
	data.motes = [int(w) for w in raw_input().split()]
	return data

def get_num_cases():
	return int(raw_input())

def print_case(case, solution):
	print 'Case #{0}: {1}'.format(case, solution)

def run():
	T = get_num_cases()
	for i in xrange(T):
		print_case(i + 1, get_data().algorithm())

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def process(arg):
	pass

def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "h", ["help"])
		except getopt.error as msg:
			raise Usage(msg)
	    # process options
		for o, a in opts:
			if o in ("-h", "--help"):
				print __doc__
				return 0
		# process arguments
		for arg in args:
			process(arg)
		run()
		return 0
	except Usage as err:
		print >>sys.stderr, err.msg
		print >>sys.stderr, "for help use --help"
		return 2

if __name__ == "__main__":
	sys.exit(main())
