from math import log10, ceil

def numDigs(x):
	return int(ceil(log10(x)))

def rotOnce(x, digs):
	mod = 10**(digs-1)
	return (x%10)*mod + (x//10)

def rot(x):
	n = numDigs(x)
	yield x
	for i in range(n-1):
		x = rotOnce(x, n)
		#print x
		if numDigs(x)==n:
			yield x

def parse(filename):
	cases = []
	fin = file(filename, 'r');
	numCases = int(fin.readline().strip())
	for i in range(numCases):
		line = fin.readline().strip()
		cases.append(Case(line))

	return cases
		
class Case(object):
	def __init__(this, line):
		start, end = map(int, line.split(' '))
		this.start = start
		this.end = end

	def solve(this):
		count = 0
		values = set(range(this.start, this.end+1))
		for x in values:
			recValues = set(rot(x))
			#print x, recValues
			if len(recValues)!=1:
				recValues = recValues & values
				if len(recValues)!=1:
					n = len(recValues)
					count += n*(n-1)/2
					values ^= recValues
		this.count = count

	def pprint(this, caseNum):
		print "Case #%d: %d"%(caseNum, this.count)

def main():
	cases = parse('C-small-attempt0.in')
	for i, x in enumerate(cases):
		x.solve()
		x.pprint(i+1)

if __name__ == '__main__':
	main()
