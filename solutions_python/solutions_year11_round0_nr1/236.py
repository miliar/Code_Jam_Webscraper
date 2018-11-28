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
		this.path = []
		this.seconds = []
		this.parse(line)

	def parse(this, line):
		line = line.strip().split(' ')
		this.numItems =	int(line[0])
		for i in range(this.numItems):
			this.path.append( (line[i*2+1], int(line[i*2+2])) )

	def solve(this):
		oPosition = 1
		bPosition = 1
		oTime = 0
		bTime = 0
		for button in this.path:
			if button[0] == 'O':
				oTime = max(oTime+abs(button[1]-oPosition), bTime)+1
				oPosition = button[1]
				#print "oTime =",oTime
			else:
				bTime = max(bTime+abs(button[1]-bPosition), oTime)+1
				bPosition = button[1]
				#print "bTime =",bTime

		this.totalTime = max(oTime, bTime)

	def pprint(this, caseNum):
		print "Case #%d: %d"%(caseNum, this.totalTime)

def main():
	cases = parse('A-large.in')
	for i, x in enumerate(cases):
		x.solve()
		x.pprint(i+1)

if __name__ == '__main__':
	main()
