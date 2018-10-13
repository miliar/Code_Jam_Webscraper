import sys
from time import time
from gcjparser import Parser

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def mcd(n,m):
	return (n/gcd(n,m))*m 

def parse(filename):
	parser = Parser(file(filename, 'r'), (int, int, int))
	for caseData in parser:
		yield Case(*caseData)
		
class Case(object):
	def __init__(this, N, PD, PG):
		this.N = N
		this.PD = PD
		this.PG = PG

	def isPossible(this):
		N = this.N
		PD = this.PD
		PG = this.PG
		if PG==100 or PG==0:
			return PG==PD

		modNd = 100/gcd(100, PD)
		modNg = 100/gcd(100, PG)

		#print modNd, modNg

		if modNd>N:
			return False

		"""maxNd = N - (N%modNd)
		minNd = maxNd/modNd"""

		return True

	def solve(this):
		this.answer = "Possible" if this.isPossible() else "Broken"

	def pprint(this, caseNum, fout):
		fout.write("Case #%d: %s\n"%(caseNum, this.answer))

def main(filein, fileout):
	start = time()

	fout = file(fileout, 'w')
	cases = parse(filein)

	for i, x in enumerate(cases):
		x.solve()
		x.pprint(i+1, fout)

	end = time()
	print "Total time=%s"%(end-start)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
