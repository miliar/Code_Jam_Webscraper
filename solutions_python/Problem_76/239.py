import sys
from time import time

def parse(filein):
	fin = file(filein, 'r')
	cases = []

	numcases = int(fin.readline().strip())

	for i in range(numcases):
		numCandies = int(fin.readline().strip())
		values = map(int, fin.readline().strip().split(' '))
		cases.append(Case(values))

	return cases

def splititerator(source):
	""" This iterator generates all posible splits of source list into two lists.
		E.g [1,2,3] => ([2, 3], [1]), ([1, 3], [2]), ([3], [1, 2]) """
	flags = [0] * len(source)
	flags = increment(flags)
	while flags[-1]==0:
		part1 = [value for value, flag in zip(source,flags) if flag==0]
		part2 = [value for value, flag in zip(source,flags) if flag==1]
		yield (part1, part2)
		flags = increment(flags)

def increment(flags):
	flags[0] += 1
	for i in range(len(flags)):
		if flags[i] == 2:
			flags[i] = 0
			flags[i+1] += 1
		else:
			return flags

def xorsum(values):
	return reduce(lambda x,y: x^y, values, 0)

class Case(object):
	def __init__(this, values):
		this.values = values


	def fastCheck(this):
		return xorsum(this.values) == 0

	def solve(this):
		this.answer = "NO"
		if this.fastCheck()==False:
			return
		else:
			maxpile = 0
			for part1, part2 in splititerator(this.values):
				if xorsum(part1) == xorsum(part2):
					maxpile = max(maxpile, sum(part1), sum(part2))
			if maxpile!=0:
				this.answer = str(maxpile)

	def pprint(this, i, out):
		out.write("Case #%d: %s\n"%(i, this.answer))


def main(filein, fileout):
	start = time()
	fout = file(fileout, 'w')

	cases = parse(filein)
	for i,x in enumerate(cases):
		x.solve()
		x.pprint(i+1, fout)

	end = time()
	print "Total time=%s"%(end-start)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
