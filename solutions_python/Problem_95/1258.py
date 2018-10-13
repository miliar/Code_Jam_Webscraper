Table = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o',
	'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 
	'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 
	'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 
	'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 
	'x': 'm', 'z': 'q'}

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
		this.input_text = line.strip()
		this.output_text = None

	def solve(this):
		def replaceChar(char):
			return Table.get(char, char)
		this.output_text = ''.join(map(replaceChar, this.input_text))

	def pprint(this, caseNum):
		print "Case #%d: %s"%(caseNum, this.output_text)

def main():
	cases = parse('A-small-attempt0.in')
	for i, x in enumerate(cases):
		x.solve()
		x.pprint(i+1)

if __name__ == '__main__':
	main()
