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
		values = map(int, line.split(' '))
		N = int(values[0])
		this.N = N
		S = int(values[1])
		this.S = S
		p = int(values[2])
		this.p = p
		this.points = map(int, values[3:3+N])

	def solve(this):
		p = this.p
		S = this.S
		def calcMaxPoint(sumpoints):
			if sumpoints%3==0:
				return sumpoints/3
			elif sumpoints%3==1:
				return (sumpoints+2)/3
			else:
				return (sumpoints+1)/3
		maxpoints = map(calcMaxPoint, this.points)
		#print maxpoints
		canSurprise = [(sp%3)!=1 for sp in this.points]
		#print canSurprise
		alreadyFitCout = len([x for x in maxpoints if x>=p])
		#print p, alreadyFitCout
		couldSurprise = len([x for x,y in zip(maxpoints, canSurprise) if x==p-1 and x>0 and y==True])

		this.answer = alreadyFitCout + min(couldSurprise, S)

	def pprint(this, caseNum):
		print "Case #%d: %d"%(caseNum, this.answer)

def main():
	cases = parse('B-large.in')
	#cases = parse('B-test.txt')
	for i, x in enumerate(cases):
		x.solve()
		x.pprint(i+1)

if __name__ == '__main__':
	main()
